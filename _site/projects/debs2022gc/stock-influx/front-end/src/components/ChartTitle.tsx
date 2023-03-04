interface Props {
  symbol: string;
}

const ChartTitle: React.FC<Props> = ({ symbol }) => {
  return (
    <div className="title-container">
      {symbol}
      <style jsx>{`
        .title-container {
          width: 80%;
          font-size: 36px;
          font-weight: 700;
          color: #323267;
          margin-top: 10px;
        }
      `}</style>
    </div>
  );
};

export default ChartTitle;
