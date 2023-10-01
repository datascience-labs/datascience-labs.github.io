import Head from "next/head";

interface Props {
  title: string;
}

const Seo: React.FC<Props> = ({ title }) => {
  return (
    <div>
      <Head>
        <title>StockInflux | {title}</title>
      </Head>
    </div>
  );
};

export default Seo;
