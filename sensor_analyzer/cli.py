import json
from pathlib import Path

import click

from .analyzer import load_data, compute_stats, detect_anomalies


@click.command()
@click.argument(
    "csv_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
@click.option(
    "--temp-min",
    type=float,
    default=15.0,
    show_default=True,
    help="Minimum acceptable temperature.",
)
@click.option(
    "--temp-max",
    type=float,
    default=30.0,
    show_default=True,
    help="Maximum acceptable temperature.",
)
@click.option(
    "--show-anomalies/--no-anomalies",
    default=True,
    show_default=True,
    help="Whether to print the detected anomalies.",
)
def main(csv_path: Path, temp_min: float, temp_max: float, show_anomalies: bool) -> None:
    """
    Analyze a CSV file containing sensor data.

    CSV_PATH: Path to the CSV file with 'temperature' and 'humidity' columns.
    """
    click.echo(f"Loading data from {csv_path}...")
    df = load_data(str(csv_path))

    click.echo("Computing statistics...")
    stats = compute_stats(df)
    click.echo("Statistics (JSON):")
    click.echo(json.dumps(stats, indent=2))

    anomalies = detect_anomalies(df, temp_min=temp_min, temp_max=temp_max)
    if show_anomalies:
        click.echo()
        click.echo(
            f"Found {len(anomalies)} anomalies "
            f"outside [{temp_min}, {temp_max}] °C:"
        )
        if len(anomalies) > 0:
            click.echo(anomalies.to_string(index=False))
        else:
            click.echo("No anomalies detected.")


if __name__ == "__main__":
    main()
