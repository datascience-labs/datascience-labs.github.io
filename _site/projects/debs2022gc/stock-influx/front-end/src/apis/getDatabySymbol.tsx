import { dev_requestDomain, requestDomain } from "../utils/url";

interface Props {
  symbol: string;
}
const getDataBySymbol = async ({ symbol }: Props) => {
  return await fetch(`${dev_requestDomain}/v1/api/symbols/${symbol}/`);
};

export default getDataBySymbol;
