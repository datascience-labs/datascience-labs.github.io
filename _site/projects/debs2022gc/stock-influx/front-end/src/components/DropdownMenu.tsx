import Image from "next/image";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { links } from "../utils/links";

const DropdownMenu: React.FC = () => {
  const dropdownRef = useRef(null);
  const [isActive, setActive] = useState(false);
  const onPress = () => setActive(!isActive);
  useEffect(() => {
    const pageClickEvent = () => {
      if (dropdownRef.current !== null) {
        setActive(!isActive);
      }
    };
    if (isActive) {
      window.addEventListener("click", pageClickEvent);
    }
    return () => {
      window.removeEventListener("click", pageClickEvent);
    };
  }, [isActive]);

  return (
    <div className="container">
      <button onClick={onPress} className="trigger">
        <Image src="/more.svg" width={40} height={17} alt="more" />
      </button>
      <nav
        ref={dropdownRef}
        className={`menu ${isActive ? "active" : "inactive"}`}
      >
        <ul>
          {links.map((val, idx) => (
            <li key={idx}>
              <Link href={val.path}>
                <a className="">{val.displayName}</a>
              </Link>
            </li>
          ))}
        </ul>
      </nav>
      <style jsx>{`
        .container {
          position: fixed;
          top: 2.5vh;
          right: 5px;
        }
        .trigger {
          background-color: transparent;
          border: 0;
        }
        .trigger:hover {
          transform: translateY(-1px);
        }
        .btnText {
          min-width: 100px;
          text-align: center;
          padding: 5px;
        }
        .menu {
          background-color: #7b7cb6;
          border-radius: 10px;
          opacity: 0;
          visibility: hidden;
          transform: translateY(-20px);
          transition: opacity 0.4s ease, transform 0.4s ease, visibility 0.4s;
        }
        .menu.active {
          opacity: 1;
          visibility: visible;
          transform: translateY(0);
        }
        .menu ul {
          list-style: none;
          padding: 0;
          margin: 0;
        }
        .menu .others {
          border-bottom: 1px solid #494949;
        }
        .menu li a {
          font-size: 14px;
          font-weight: 700;
          text-decoration: none;
          padding: 15px 20px;
          display: block;
          color: #fff;
        }
      `}</style>
    </div>
  );
};

export default DropdownMenu;
