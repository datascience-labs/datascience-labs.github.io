import { useRouter } from "next/router";
import getSymbols from "../apis/getSymbols";
import { Line } from "rc-progress";
import { useEffect, useState } from "react";
const MarketList = () => {
  const router = useRouter();
  const [percent, setPercent] = useState(0);
  const [input, setInput] = useState("");
  const [symbols, setSymbols] = useState<string[]>([]);
  useEffect(() => {
    getSymbols()
      .then((res) => res.json())
      .then((json) => setSymbols(json.data))
      .catch((e) => console.log(e))
      .finally(() => console.log("done"));
  }, []);
  useEffect(() => {
    const increase = () => {
      if (percent >= 100) return;
      setPercent(percent + 3);
    };
    increase();
  }, [percent]);

  return (
    <div className="container">
      <h1>Real Time Quotes Monitor</h1>
      <div className="input-container">
        <h2>Filter</h2>
        <input value={input} onChange={(e) => setInput(e.target.value)} />
      </div>
      {symbols.length ? (
        <ul>
          {symbols
            .filter((v) => v.includes(input.toUpperCase()))
            .reverse()
            .map((val, idx) => (
              <li
                className="item-container"
                key={idx}
                onClick={() => router.push("/chart", { query: val })}
              >
                <h3>{val}</h3>
              </li>
            ))}
        </ul>
      ) : (
        <div className="loading">
          <Line percent={percent} strokeWidth={4} strokeColor="#6667ab" />
        </div>
      )}
      <style jsx>{`
        h1 {
          display: flex;
          width: 90%;
          align-self: center;
          color: #323267;
        }
        .container {
          width: 80%;
          display: flex;
          margin: 0 auto;
          flex-direction: column;
        }
        .input-container {
          align-self: flex-end;
          align-items: center;
          display: flex;
          color: #323267;
        }
        input {
          margin-left: 10px;
          font-size: 16px;
          font-weight: 500;
        }
        .loading {
          display: flex;
          width: 200px;
          height: 400px;
          justify-content: center;
          align-items: center;
          margin: 0 auto;
          color: #6667ab;
        }
        h1 {
          text-align: center;
        }
        ul {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        }
        .item-container {
          list-style: none;
          color: #fff;
          margin: 5px;
          background-color: #6667ab60;
          display: flex;
          justify-content: center;
          align-items: center;
          border-radius: 16px;
          cursor: pointer;
        }
        .item-container:hover {
          transform: translateY(2px);
        }
        .item-container::after {
          opacity: 0.8;
        }
      `}</style>
    </div>
  );
};

export default MarketList;
