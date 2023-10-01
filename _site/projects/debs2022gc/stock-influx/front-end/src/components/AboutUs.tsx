import Image from "next/image";
import Link from "next/link";
import useScrollFadeIn from "../hooks/useScrollFadeIn";

const AboutUs: React.FC = () => {
  const animatedImage = useScrollFadeIn();
  const animatedBtn = useScrollFadeIn("right", 1, 0.2);
  const memberList = [
    { name: "Suyeon Wang", email: "wangsunny6143@gmail.com" },
    { name: "Jaekyung Kim", email: "2143575@donga.ac.kr" },
    { name: "Jinseong Hwang", email: "jinseong.dev@gmail.com" },
    { name: "Yoonsang Yang", email: "yoonsang.developer@gmail.com" },
    { name: "Jungkyu Han", email: "jkhan@dau.ac.kr" },
    { name: "Sejin Chun", email: "sjchun@dau.ac.kr" },
  ];
  return (
    <div className="container">
      <div className="title">
        <h1>ABOUT US</h1>
      </div>
      <div className="content-container">
        <div {...animatedImage} className="image-container">
          <Image src={"/about.jpg"} width={1280} height={720} alt="about" />
        </div>
        <div {...animatedBtn} className="list-container">
          {memberList.map((val, idx) => (
            <li key={idx} className="item">
              <h2>{val.name}</h2>
              <Link href={"mailto:" + val.email}>
                <a>{val.email}</a>
              </Link>
            </li>
          ))}
        </div>
      </div>
      <style jsx>{`
        .container {
          display: flex;
          flex-direction: column;
          margin: 0 auto;
          justify-content: center;
          width: 80%;
        }
        .title {
          display: flex;
        }
        .image-container {
          height: 50vh;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        .content-container {
          display: flex;
        }
        .list-container {
          display: flex;
          flex-direction: column;
          list-style: none;
          width: 100%;
          align-self: center;
          align-items: center;
          justify-content: center;
        }
        .item {
          border-radius: 36px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          margin-bottom: 50px;
        }
        @media (max-width: 1000px) {
          .item {
            width: 15rem;
            height: 8rem;
            border-radius: 36px;
          }
          h1 {
            font-size: 1.5rem;
          }
        }
      `}</style>
    </div>
  );
};

export default AboutUs;
