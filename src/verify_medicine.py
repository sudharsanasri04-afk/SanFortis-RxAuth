"""
verify_medicine.py
~~~~~~~~~~~~~~~~~~~

A simple command-line tool that demonstrates how to verify the authenticity of
medicine packaging using a cryptographic hash.  Given a medicine's serial
number, manufacturer and expiry date, the script computes a SHA-256 hash and
compares it to an expected value stored in a sample dataset.

This script is part of the SanFortis-RxAuth project.  It is not intended for
production use.
"""

import argparse
import json
import hashlib
from pathlib import Path
from typing import Tuple, Optional, Dict, Any

# Path to the sample medicines dataset.  The file contains a list of
# dictionaries, each with a name, manufacturer, serial_number, expiry_date and
# a precomputed hash.
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "medications.json"


def load_medications() -> list:
    """Load the sample medicines from the JSON file.

    Returns
    -------
    list
        A list of medication records.
    """
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_FILE}")
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def compute_hash(serial_number: str, manufacturer: str, expiry_date: str) -> str:
    """Compute the SHA-256 hash of the medicine details.

    The hash is computed over the string "serial_number|manufacturer|expiry_date".

    Parameters
    ----------
    serial_number : str
        The serial number of the medicine.
    manufacturer : str
        The name of the manufacturer.
    expiry_date : str
        The expiry date in YYYY-MM-DD format.

    Returns
    -------
    str
        The hex-encoded SHA-256 hash.
    """
    data_str = f"{serial_number}|{manufacturer}|{expiry_date}"
    return hashlib.sha256(data_str.encode("utf-8")).hexdigest()


def verify_medicine(serial_number: str, manufacturer: str, expiry_date: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """Verify a medicine's authenticity.

    Parameters
    ----------
    serial_number : str
        Serial number of the medicine to verify.
    manufacturer : str
        Manufacturer name supplied by the user.
    expiry_date : str
        Expiry date supplied by the user (YYYY-MM-DD).

    Returns
    -------
    tuple
        A tuple `(is_authentic, record)` where `is_authentic` is True if the
        details match the stored hash, and `record` is the matching record
        (or None if no record was found).
    """
    medicines = load_medications()
    computed_hash = compute_hash(serial_number, manufacturer, expiry_date)
    for med in medicines:
        if med.get("serial_number") == serial_number:
            expected_hash = med.get("hash")
            # Also cross-validate manufacturer and expiry in case the same
            # serial number exists for different batches.
            if (
                med.get("manufacturer") == manufacturer
                and med.get("expiry_date") == expiry_date
                and expected_hash == computed_hash
            ):
                return True, med
            else:
                return False, med
    return False, None


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Verify medicine authenticity by comparing a SHA-256 hash of the "
            "serial number, manufacturer and expiry date against a sample dataset."
        )
    )
    parser.add_argument(
        "--serial", required=True, help="Medicine serial number (e.g. HC12345)"
    )
    parser.add_argument(
        "--manufacturer", required=True, help="Medicine manufacturer (case sensitive)"
    )
    parser.add_argument(
        "--expiry", required=True, help="Expiry date in YYYY-MM-DD format"
    )
    args = parser.parse_args()

    is_authentic, med_record = verify_medicine(
        args.serial, args.manufacturer, args.expiry
    )

    if med_record is None:
        print(f"No record found for serial number '{args.serial}'.")
    elif is_authentic:
        print(
            "✅ Medicine is authentic:"
            + f" {med_record['name']} by {med_record['manufacturer']} (batch {med_record['serial_number']})."
        )
    else:
        print(
            "⚠️ Potential counterfeit detected! Provided details do not match the expected hash."
        )


if __name__ == "__main__":
    main()
