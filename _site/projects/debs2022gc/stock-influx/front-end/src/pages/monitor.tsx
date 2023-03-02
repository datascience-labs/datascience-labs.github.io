import type { NextPage } from "next";
import MarketList from "../components/MarketList";
import Seo from "../components/Seo";

const Market: NextPage = () => {
  return (
    <div>
      <Seo title="Mointor" />
      <MarketList />
    </div>
  );
};

export default Market;
