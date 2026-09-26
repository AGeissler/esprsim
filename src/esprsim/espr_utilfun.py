#!/usr/bin/env python3
"""
Module contains utility functions for esprsim.
"""
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from collections import defaultdict


def generate_datetime_index(year, from_month, from_day, to_month, to_day,
                            steps_per_hour, existing_df=None):
    r"""
    Generate a datetime timestamp series and attach it as index to an existing dataframe.
    
    Parameters:
    - year: str, e.g., '2024'
    - from_month: str, e.g., '1' or '01'
    - from_day: str, e.g., '15'
    - to_month: str, e.g., '2' or '02'
    - to_day: str, e.g., '10'
    - steps_per_hour: str or int, number of timestamps per hour (e.g., '4' for 15-min intervals)
    - existing_df: pd.DataFrame, optional dataframe to attach the index to
    
    Returns:
    - pd.DatetimeIndex if existing_df is None, otherwise the dataframe with new index

    Note:
      Code by PerplexityAI.
    """
    # Convert all inputs to integers
    year = int(year)
    from_month = int(from_month)
    from_day = int(from_day)
    to_month = int(to_month)
    to_day = int(to_day)
    steps_per_hour = int(steps_per_hour)

    # Create start and end datetime
    start_dt = datetime(year, from_month, from_day, 0, 0, 0)
    end_dt = datetime(year, to_month, to_day, 23, 59, 59)

    # Calculate interval in minutes
    interval_minutes = 60 / steps_per_hour

    # Generate the datetime range
    datetime_index = pd.date_range(start=start_dt, end=end_dt, freq=f'{interval_minutes}min')

    if existing_df is not None:
        # Trim or extend the index to match dataframe length
        if len(datetime_index) >= len(existing_df):
            datetime_index = datetime_index[:len(existing_df)]
        else:
            # If not enough timestamps, extend with the last frequency
            extra_needed = len(existing_df) - len(datetime_index)
            last_dt = datetime_index[-1]
            extra_index = pd.date_range(
                start=last_dt + pd.Timedelta(minutes=interval_minutes),
                periods=extra_needed,
                freq=f'{interval_minutes}min'
            )
            datetime_index = datetime_index.append(extra_index)

        existing_df.index = datetime_index
        return existing_df

    return datetime_index

def get_timestep_hours(df):
    """
    Extract the time-step duration in decimal hours from a dataframe's DatetimeIndex.
    
    Parameters:
    - df: pd.DataFrame with a DatetimeIndex
    
    Returns:
    - float: time-step duration in hours (e.g., 0.25 for 15-minute intervals)

    Note:
      Code by PerplexityAI.
    """
    if len(df) < 2:
        raise ValueError("Dataframe must have at least 2 rows to calculate timestep")

    # Calculate the difference between consecutive index values
    timestep = df.index[1] - df.index[0]

    # Convert to hours (total_seconds() / 3600)
    return timestep.total_seconds() / 3600


def aggregate_pv_by_zone(df, zone_groups=['Z00', 'Z20', 'Z40']):
    r"""
    Aggregate PV power columns by zone group (default 'Z00', 'Z20', 'Z40').
    Converts W to kWh using the dataframe's timestep.

    Parameters:
    - df: pd.DataFrame with PV power columns (in W) and DatetimeIndex
    - zone_groups: list of zone strings to group by

    Returns:
    - dict: {zone: total_energy_kWh} for each zone group

    Note:
      The physics: if you have power readings in W at regular intervals :math:`\Delta t`
      (hours), the energy is:

      .. math::
         E\,=\,\sum{i}P_i\,×\,\Delta t

      So summing all W values, multiplying by the timestep (and dividing by 1000) gives
      kWh.

    Code by PerplexityAI.
    """
    if len(df) < 2:
        raise ValueError("Dataframe must have at least 2 rows")

    # Get timestep in hours from the index
    timestep_hours = (df.index[1] - df.index[0]).total_seconds() / 3600

    zone_totals = {zone: 0.0 for zone in zone_groups}

    for col in df.columns:
        if 'pv power' in col.lower():
            for zone in zone_groups:
                if zone in col:
                    # Sum power (W), multiply by timestep (h) and divide by W/kW to get
                    # energy in (kWh)
                    zone_totals[zone] += df[col].sum() * timestep_hours / 1000
                    break

    return zone_totals

def plot_pv_bars_matplotlib(data_dict, zone_groups=['Z00', 'Z20', 'Z40'],
                            figsize=(10, 6), colors=['#3498db', '#e74c3c', '#2ecc71'],
                            save_path=None):
    """
    Create a grouped bar chart showing PV yield by zone for each case.
    
    Parameters:
    - data_dict: dict of {case_name: dataframe}
    - zone_groups: list of zone strings to group by
    - figsize: tuple (width, height)
    - colors: list of colors for each zone group
    - save_path: optional path to save the figure
    """
    cases = list(data_dict.keys())
    n_cases = len(cases)
    n_zones = len(zone_groups)

    # Calculate aggregated values
    data_matrix = np.zeros((n_cases, n_zones))
    for i, case in enumerate(cases):
        zone_totals = aggregate_pv_by_zone(data_dict[case], zone_groups)
        for j, zone in enumerate(zone_groups):
            data_matrix[i, j] = zone_totals[zone]

    # Create plot
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(n_cases)
    bar_width = 0.8 / n_zones

    for j, zone in enumerate(zone_groups):
        offset = (j - n_zones/2 + 0.5) * bar_width
        ax.bar(x + offset, data_matrix[:, j], bar_width * 0.9,
               label=zone, color=colors[j % len(colors)],
               edgecolor='white', linewidth=0.5)

    ax.set_xlabel('Case')
    ax.set_ylabel('Total PV Yield (kWh)')
    ax.set_title('PV Yield by Zone Group')
    ax.set_xticks(x)
    ax.set_xticklabels(cases)
    ax.legend(title='Zone')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    fig.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig

def plot_pv_bars_plotly(data_dict, zone_groups=['Z00', 'Z20', 'Z40'],
                        colors=['#3498db', '#e74c3c', '#2ecc71'],
                        title='PV Yield by Zone Group',
                        save_path=None):
    """
    Create an interactive grouped bar chart showing PV yield by zone for each case.
    
    Parameters:
    - data_dict: dict of {case_name: dataframe}
    - zone_groups: list of zone strings to group by
    - colors: list of colors for each zone group
    - title: plot title
    - save_path: optional path to save the figure as HTML
    """
    cases = list(data_dict.keys())
    n_cases = len(cases)
    n_zones = len(zone_groups)

    # Calculate aggregated values
    data_matrix = np.zeros((n_cases, n_zones))
    for i, case in enumerate(cases):
        zone_totals = aggregate_pv_by_zone(data_dict[case], zone_groups)
        for j, zone in enumerate(zone_groups):
            data_matrix[i, j] = zone_totals[zone]

    # Create traces
    traces = []
    for j, zone in enumerate(zone_groups):
        trace = go.Bar(
            x=cases,
            y=data_matrix[:, j],
            name=zone,
            marker_color=colors[j % len(colors)],
            hovertemplate=f'<b>{zone}</b><br>Yield: %{{y:.0f}} kWh<extra></extra>'
        )
        traces.append(trace)

    fig = go.Figure(data=traces)

    fig.update_layout(
        title=title,
        xaxis_title='Case',
        yaxis_title='Total PV Yield (kWh)',
        barmode='group',
        bargap=0.15,
        bargroupgap=0.1,
        hovermode='x unified',
        legend_title='Zone',
        height=500,
        width=800
    )

    if save_path:
        fig.write_html(save_path)

    return fig


if __name__ == "__main__":
    # === Create three sample dataframes ===
    idx_15min = pd.date_range('2024-01-15 00:00', periods=96, freq='15min')
    idx_30min = pd.date_range('2024-01-15 00:00', periods=48, freq='30min')
    idx_1h = pd.date_range('2024-01-15 00:00', periods=24, freq='1h')

    df1 = pd.DataFrame({
        'building:spmatl:Z00 E2:misc data:pv power (W)': np.random.uniform(200, 400, 96),
        'building:spmatl:Z20 E2:misc data:pv power (W)': np.random.uniform(200, 400, 96),
        'building:spmatl:Z40 E2:misc data:pv power (W)': np.random.uniform(200, 400, 96),
    }, index=idx_15min)

    df2 = pd.DataFrame({
        'building:spmatl:Z00 E2:misc data:pv power (W)': np.random.uniform(250, 450, 48),
        'building:spmatl:Z20 E2:misc data:pv power (W)': np.random.uniform(250, 450, 48),
        'building:spmatl:Z40 E2:misc data:pv power (W)': np.random.uniform(250, 450, 48),
    }, index=idx_30min)

    df3 = pd.DataFrame({
        'building:spmatl:Z00 E2:misc data:pv power (W)': np.random.uniform(300, 500, 24),
        'building:spmatl:Z20 E2:misc data:pv power (W)': np.random.uniform(300, 500, 24),
        'building:spmatl:Z40 E2:misc data:pv power (W)': np.random.uniform(300, 500, 24),
    }, index=idx_1h)
    # Your dict of dataframes
    results_dict = {
        'Case 1': df1,
        'Case 2': df2,
        'Case 3': df3
    }

    # Matplotlib version
    fig, ax = plot_pv_bars_matplotlib(results_dict)
    plt.show()

    # Plotly version (interactive)
    fig = plot_pv_bars_plotly(results_dict)
    fig.show()

    # Save Plotly as HTML
    plot_pv_bars_plotly(results_dict, save_path='pv_power_by_zone.html')

    # Test aggregation
    for name, df in results_dict.items():
        totals = aggregate_pv_by_zone(df)
        print(f"{name}: {totals}")
