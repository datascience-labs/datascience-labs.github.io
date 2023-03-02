import type { NextPage } from "next";
import IndexCross from "../components/IndexCross";
import IndexDesc from "../components/IndexDesc";
import IndexTitle from "../components/IndexTitle";
import Seo from "../components/Seo";

const Home: NextPage = () => {
  return (
    <div>
      <Seo title="Home" />
      <IndexTitle />
      <IndexCross />
      <IndexDesc />
    </div>
  );
};

export default Home;
