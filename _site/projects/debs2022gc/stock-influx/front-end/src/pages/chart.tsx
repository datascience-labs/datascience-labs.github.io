import { NextPage } from "next";
import { useRouter } from "next/router";
import ChartBar from "../components/ChartBar";
import ChartTitle from "../components/ChartTitle";
import Seo from "../components/Seo";

const ChartPage: NextPage = () => {
  const router = useRouter();
  const symbol = router.asPath.split("?")[1];

  return (
    <div className="container">
      <Seo title="Chart" />
      <ChartTitle symbol={symbol} />
      <ChartBar symbol={symbol} />
      <style jsx>{`
        .container {
          display: flex;
          flex-direction: column;
          align-items: center;
        }
      `}</style>
    </div>
  );
};

export default ChartPage;
