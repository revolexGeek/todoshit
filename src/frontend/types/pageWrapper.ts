export default interface IPageNumberPagination<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}
