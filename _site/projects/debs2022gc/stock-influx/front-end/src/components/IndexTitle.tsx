import Link from "next/link";
import useScrollFadeIn from "../hooks/useScrollFadeIn";

const IndexTitle = () => {
  const animatedTitle = useScrollFadeIn();
  const animatedBtn = useScrollFadeIn("up", 1, 0.2);

  return (
    <div className="container">
      <div {...animatedTitle} className="title">
        <h1>StockInflux</h1>
        <h2>Scalable and Fast Web App</h2>
      </div>
      <div {...animatedBtn} className="go-market">
        <Link href={"/monitor"}>
          <a>Monitor</a>
        </Link>
      </div>
      <style jsx>{`
        .container {
          display: flex;
          align-items: center;
          width: 100%;
          height: 80vh;
          background-image: linear-gradient(
              to bottom,
              rgba(102, 103, 171, 0.5),
              rgba(57, 57, 67, 0.5)
            ),
            url("/chart.jpg");
          margin: 0;
        }
        .title {
          width: 40%;
          margin-left: 20vw;
          display: flex;
          flex-direction: column;
          justify-content: center;
        }
        h1 {
          font-size: 3rem;
          font-weight: 900;
          color: #eff8ff;
          margin-top: 0;
        }
        h2 {
          color: #eff8ff;
          margin-top: 0;
        }
        .go-market {
          display: flex;
          background-color: #6667ab;
          border-radius: 24px;
          justify-content: center;
          align-items: center;
          width: 10rem;
          height: 4rem;
          box-shadow: 1px 3px 1px 1px #000;
        }
        .go-market a {
          text-decoration: none;
          color: #eff8ff;
          font-size: 1.5rem;
        }
        @media (max-width: 800px) {
          .title {
            margin-left: 0;
          }
          h1 {
            font-size: 2rem;
          }
          .container {
            flex-direction: column;
            justify-content: center;
            align-items: center;
          }
        }
      `}</style>
    </div>
  );
};

export default IndexTitle;
