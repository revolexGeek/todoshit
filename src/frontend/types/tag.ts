export default interface ITag {
  id: number | string;
  name: string;
  color: TagColor;
}

export enum TagColor {
  "red",
  "orange",
  "amber",
  "yellow",
  "lime",
  "green",
  "emerald",
  "teal",
  "cyan",
  "sky",
  "blue",
  "indigo",
  "violet",
  "purple",
  "pink",
  "rose",
  "gray",
  "white",
  "black",
  "primary",
}
