import Image from "next/image";
import useScrollFadeIn from "../hooks/useScrollFadeIn";

const IndexCross = () => {
  const animatedCross = useScrollFadeIn("right", 1, 0);
  const animatedText = useScrollFadeIn("left", 1, 0);

  return (
    <div className="container">
      <div {...animatedCross} className="cross">
        <Image
          src={"/cross.svg"}
          width={909}
          height={300}
          alt={"cross-chart"}
        />
      </div>
      <div {...animatedText} className="desc">
        We calculate by analyzing trend indicators using stock big data.
      </div>
      <style jsx>{`
        .container {
          width: 100%;
          height: 60vh;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        .cross {
          background-color: #eff8ff;
          display: flex;
          justify-content: center;
          align-items: center;
          padding: 10px;
          border-radius: 36px;
          margin-bottom: 50px;
          margin-right: 100px;
        }
        .desc {
          font-size: 2rem;
          text-shadow: 2px 2px 2px gray;
          font-weight: 900;
          color: #fff;
          margin-top: 50px;
          margin-left: 100px;
          text-align: right;
        }
        @media (max-width: 800px) {
          .cross {
            width: 80%;
            margin: 0;
          }
          .desc {
            font-size: 1.5rem;
            margin-left: 0;
            margin-right: 30px;
          }
        }
      `}</style>
    </div>
  );
};

export default IndexCross;
