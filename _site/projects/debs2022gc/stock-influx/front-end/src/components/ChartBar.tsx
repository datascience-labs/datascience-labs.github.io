import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { Line } from "react-chartjs-2";
import getDataBySymbol from "../apis/getDatabySymbol";
import { ChartData } from "../utils/types";

interface Props {
  symbol: string;
}

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const ChartBar: React.FC<Props> = ({ symbol }) => {
  const [chartData, setChartData] = useState<ChartData[]>([]);
  const [time, setTime] = useState(0);
  const router = useRouter();
  useEffect(() => {
    if (!symbol) router.replace("/monitor");
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [symbol]);

  useEffect(() => {
    (async () => {
      await getDataBySymbol({ symbol: symbol })
        .then((res) => res.json())
        .then((json) => setChartData(json.data))
        .catch((e) => console.log(e))
        .finally(() => console.log("done"));
    })();
    setTimeout(() => setTime(time + 1), 20000);
  }, [time, symbol]);
  const options = {
    responsive: true,
    plugins: {},
  };
  const labels = chartData.map(
    (val) => val.lastTradeTime.split("T")[1].split("Z")[0].split(".")[0]
  );
  const data = {
    labels,
    datasets: [
      {
        label: symbol,
        backgroundColor: "#6667ab",
        data: chartData?.map((val) => val.lastTradePrice),
      },
    ],
  };
  return (
    <div className="container">
      <div className="chart-info">
        X : Time
        <br />Y : Stock Price
      </div>
      <Line options={options} data={data} />

      <style jsx>{`
        .container {
          width: 90%;
        }
        .chart-info {
          display: flex;
          justify-content: flex-end;
          position: absolute;
          top: 10vh;
          right: 30px;
          background-color: #7b7cb6;
          color: #fff;
          font-weight: 700;
          font-size: 15px;
          padding: 5px;
          border-radius: 8px;
          box-shadow: 3px 2px 2px #000;
        }
      `}</style>
    </div>
  );
};

export default ChartBar;
