import type ITag from "~/types/tag";

export default interface ITicket {
  id: number | string;
  title: string;
  description: string;
  created_at: string;
  tags: ITag[];
}
