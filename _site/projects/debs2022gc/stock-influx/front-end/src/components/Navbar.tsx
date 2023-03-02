import Image from "next/image";
import Link from "next/link";
import { useRouter } from "next/router";
import { links } from "../utils/links";
import DropdownMenu from "./DropdownMenu";

interface Props {}

const Navbar: React.FC<Props> = () => {
  const route = useRouter().route;
  return (
    <div className="navbar">
      <div className="nav">
        <Link href={"/"}>
          <a className={route === "/" ? "logo this" : "logo"}>
            <h3>
              Stock
              <br />
              Influx
            </h3>
          </a>
        </Link>
        <div className="mob-menu">
          <DropdownMenu />
        </div>
        <div className="web-menu">
          {links.map((val, idx) => (
            <Link href={val.path} key={idx}>
              <a className={route === val.path ? "this" : ""}>
                {val.displayName}
              </a>
            </Link>
          ))}
        </div>
      </div>
      <style jsx>{`
        .navbar {
          z-index: 999;
          position: fixed;
          top: 0;
          left: 0;
          width: 100vw;
          height: 9vh;
          background-color: rgba(102, 103, 171, 0.8);
        }
        .nav {
          width: 80%;
          height: 100%;
          margin: 0 auto;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        a {
          text-decoration: none;
          color: #eff8ff;
          font-size: 1.3rem;
          padding: 10px;
        }
        h3 {
          margin: 0;
        }
        a:hover {
          transform: translateY(1px);
        }
        .logo {
          border: 5px solid #eff8ff;
          box-shadow: 3px 2px 2px #000;
        }
        .this {
          color: pink;
          border-color: #d0b4ff;
        }
        .web-menu {
          display: flex;
          width: 60%;
          justify-content: space-between;
        }
        .mob-menu {
          display: none;
        }

        @media (max-width: 800px) {
          .web-menu {
            display: none;
          }
          .mob-menu {
            display: flex;
          }
        }
      `}</style>
    </div>
  );
};

export default Navbar;
