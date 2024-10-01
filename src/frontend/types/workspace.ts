import type ITag from "~/types/tag";

export default interface IWorkspace {
  id: number | string;
  name: string;
  ticket_count: number;
  tags: ITag[];
}
