"""
Generic Code Generator

Example:
    Cst-000001
    Pro-000001
    Ord-000001
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

def generate_code(
        db: Session,
        model,
        code_column: str,
        prefix: str,
        digits: int = 6
) -> str:
    
    """
    Generate the next business code.

    Example:
        generate_code(
            db,
            Customer,
            "customer_code",
            "Cst-"
        )

        Returns:
            Cst-000051
    """

    # Get the model attribute dynamically
    column = getattr(model, code_column)

    # Fetch the latest code in descending order
    stmt = (
        select(column)
        .order_by(column.desc())
        .limit(1)
    )

    last_code = db.scalar(stmt)

    # No records found
    if last_code is None:
        return f"{prefix}{1:0{digits}d}"
    
    # Extract numeric part
    number = int(last_code.replace(prefix, ""))

    # Increment
    number += 1

    # Format with leading zeros
    return f"{prefix}{number:0{digits}d}"