import Link from "next/link";
import Navbar from "./Navbar";

const Layout = () => {
  return (
    <div className="page-container">
      <Navbar />
      <style jsx global>{`
        body {
          padding-top: 9vh; // Nav
          background-color: #c5c5de;
          margin: 0;
        }
      `}</style>
    </div>
  );
};

export default Layout;
