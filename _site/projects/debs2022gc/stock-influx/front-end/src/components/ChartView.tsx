interface Props {
  symbol: string;
}

const ChartView: React.FC<Props> = ({ symbol }) => {
  return (
    <div className="container">
      <div className="title-container">
        <h1>{symbol}</h1>
      </div>
    </div>
  );
};

export default ChartView;
