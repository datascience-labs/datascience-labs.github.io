import { NextPage } from "next";
import AboutUs from "../components/AboutUs";
import Seo from "../components/Seo";

const About: NextPage = () => {
  return (
    <div className="container">
      <Seo title="About" />
      <AboutUs />
    </div>
  );
};

export default About;
