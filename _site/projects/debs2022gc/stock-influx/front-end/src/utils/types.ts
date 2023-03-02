interface ChartData {
  lastTradePrice: number;
  lastTradeTime: string;
}

interface SymbolsType {
  code: number;
  data: string[];
  description: string;
}
export type { ChartData, SymbolsType };
