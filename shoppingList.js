// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const sampleItems = [
  {
    name: "TV",
    id: 876234812,
  },
];

class ShoppingList extends React.Component {
  constructor(props) {
    const { items } = props;
    super(props);
    this.state = { items };
    this.removeItem = this.removeItem.bind(this);
  }
  removeItem(id) {
    const itemsCopy = [...this.state.items];
    const itemIndex = this.state.items.findIndex((elem) => elem.id === id);
    itemsCopy.splice(itemIndex, 1);
    this.setState({
      items: itemsCopy,
    });
  }
  render() {
    return (
      <ul>
        {this.state.items.map((item) => (
          <li key={item.id}>
            {" "}
            {item.name}
            <button
              id="removeBtn"
              onClick={() => this.removeItem(item.id)}
              type="button"
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    );
  }
}

document.body.innerHTML = "<div id='root'> </div>";
const rootElement = document.getElementById("root");
ReactDOM.render(<ShoppingList items={sampleItems} />, rootElement);
document.getElementById("removeBtn").click();
setTimeout(() => console.log(rootElement.innerHTML));
