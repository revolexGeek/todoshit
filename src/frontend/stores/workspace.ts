import { defineStore } from "pinia";
import type IPageNumberPagination from "~/types/pageWrapper";
import type ITag from "~/types/tag";
import type ITicket from "~/types/ticket";
import type IWorkspace from "~/types/workspace";

const BASE_URL = "http://127.0.0.1:8000/api";

export const useWorkspaceStore = defineStore("workspace", {
  state: () => ({
    selectedWorkspace: null as IWorkspace | null,
    tags: [] as ITag[],
    tickets: [] as ITicket[],
    workspaces: [] as IWorkspace[],
  }),
  actions: {
    async reset() {
      this.selectedWorkspace = null;
      this.tags = [];
      this.tickets = [];
      this.workspaces = [];
    },
    async refetchAll() {
      await Promise.resolve([this.fetchWorkspaces(), this.fetchTickets()]);
    },
    async swapWorkspace(workspace: IWorkspace) {
      const toast = useToast();
      await this.reset();
      toast.add({
        title: "Смена окружения",
        description: `В данный момент происходит смена окружения на ${workspace.name}...`,
        color: "blue",
      });
      this.selectedWorkspace = workspace;
      if (this.selectedWorkspace) {
        toast.add({
          title: "Окружение сменено успешно!",
          description: `Было установлено окружение ${workspace.name}.`,
        });
        Promise.resolve([this.fetchTickets(), this.fetchWorkspaces()]);
      } else {
        toast.add({
          title: "Смена окружения не удалась!",
          description: `По каким-то причинам не удалось сменить окружение.`,
          color: "red",
        });
      }
    },
    async fetchWorkspaces() {
      const { token } = useAuth();
      const toast = useToast();

      await useFetch<IPageNumberPagination<IWorkspace>>(
        BASE_URL + "/workspaces/",
        {
          headers: {
            authorization: `${token.value}`,
          },
        }
      )
        .then((response) => {
          this.workspaces = response.data.value?.results || [];
        })
        .catch((error) => {
          this.workspaces = [];
          toast.add({
            title: "Не удалось получить окружения!",
            description: "Возможно, что-то сломалось :(",
            color: "red",
          });
        });
    },
    async fetchTickets(page: number | string = 1) {
      const { token } = useAuth();
      const toast = useToast();

      if (
        !this.selectedWorkspace ||
        !this.selectedWorkspace.id ||
        this.selectedWorkspace === null
      ) {
        toast.add({
          title: "Не удалось получить тикеты!",
          description: "Окружение не было установлено.",
          color: "red",
        });
        return;
      }

      await useFetch<IPageNumberPagination<ITicket>>(BASE_URL + "/tickets/", {
        query: {
          page: page,
          workspace__id: this.selectedWorkspace.id,
        },
        headers: {
          authorization: `${token.value}`,
        },
      })
        .then((response) => {
          if (response.data.value) {
            this.tickets = response.data.value.results;
          } else {
            this.tickets = [];
          }
        })
        .catch((error) => {
          this.tickets = [];
          toast.add({
            title: "Не удалось получить тикеты!",
            description: "Возможно, что-то сломалось :(",
            color: "red",
          });
        });
    },
    async createWorkspace(name: string) {
      const { token } = useAuth();
      const toast = useToast();
      await $fetch(BASE_URL + "/workspaces/", {
        method: "POST",
        body: {
          name: name,
        },
        headers: {
          authorization: `${token.value}`,
        },
      })
        .then((response) => {
          toast.add({
            title: "Окружение было создано!",
            description:
              "Вы можете сменить окружение через панель управления окружениями.",
          });
        })
        .catch((error) => {
          toast.add({
            title: "Не удалось создать окружение!",
            description:
              "Произошла ошибка создания окружения, попробуйте позднее.",
            color: "red",
          });
        });
    },
    async deleteWorkspace(id: number | string) {
      const { token } = useAuth();
      const toast = useToast();
      await $fetch(BASE_URL + `/workspaces/${id}/`, {
        method: "DELETE",
        headers: {
          authorization: `${token.value}`,
        },
      })
        .then((response) => {
          toast.add({
            title: "Окружение было удалено!",
            description: "Больше его нет.",
          });
          if (this.selectedWorkspace && this.selectedWorkspace.id === id) {
            this.selectedWorkspace = null;
          }
        })
        .catch((error) => {
          toast.add({
            title: "Не удалось удалить окружение!",
            description:
              "Произошла ошибка удаления окружения, попробуйте позднее.",
            color: "red",
          });
        });
    },
    async patchWorkspace(id: number | string, name: string) {
      const { token } = useAuth();
      const toast = useToast();
      await $fetch<{ name: string }>(BASE_URL + `/workspaces/${id}/`, {
        method: "PATCH",
        body: {
          name: name,
        },
        headers: {
          authorization: `${token.value}`,
        },
      })
        .then((response) => {
          if (this.selectedWorkspace && this.selectedWorkspace.id === id) {
            this.selectedWorkspace.name = response.name;
          }
          toast.add({
            title: "Название окружения было изменено!",
            description: `Теперь оно называется ${name}.`,
          });
        })
        .catch((error) => {
          toast.add({
            title: "Не удалось изменить название окружение!",
            description:
              "Произошла ошибка изменения окружения, попробуйте позднее.",
            color: "red",
          });
        });
    },
  },
});
