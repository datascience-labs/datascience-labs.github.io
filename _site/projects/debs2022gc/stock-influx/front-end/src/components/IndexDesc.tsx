import useScrollFadeIn from "../hooks/useScrollFadeIn";

const IndexDesc = () => {
  const animatedDesc = useScrollFadeIn("down", 1, 0.1);
  return (
    <div className="container">
      <section>
        <div className="desc" {...animatedDesc}>
          We can help you decide to buy or sell.
        </div>
      </section>
      <style jsx>{`
        .container {
          display: flex;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 50vh;
          background-size: 100vw;
          background-image: linear-gradient(
              to bottom,
              rgba(0, 0, 0, 0.2),
              rgba(102, 103, 171, 0.9)
            ),
            url("/ema.png");
        }
        section {
          padding-top: 10vh;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        .desc {
          text-align: center;
          font-size: 2rem;
          font-weight: 900;
          color: #fff;
          text-shadow: 2px 2px 2px #797979;
        }
        @media (max-width: 800px) {
          .desc {
            width: 80%;

            font-size: 1.5rem;
          }
        }
      `}</style>
    </div>
  );
};

export default IndexDesc;
