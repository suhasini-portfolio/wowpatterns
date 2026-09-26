type ProductCardProps = {
  name: string;
  price: number;
};

function ProductCard({ name, price }: ProductCardProps) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "16px",
        margin: "10px",
        width: "200px",
      }}
    >
      <h2>{name}</h2>
      <p>Price: ₹{price}</p>
      <button type="button">Add to Cart</button>
    </div>
  );
}

export default ProductCard;