<template>
  <UButtonGroup>
    <UBadge
      @click="setWorkspace(workspace_)"
      class="hover:cursor-pointer"
      :color="[
        workspace_.id === workspace.selectedWorkspace?.id ? 'primary' : 'gray',
      ]"
    >
      {{ workspace_.name }}
    </UBadge>
    <WorkspaceEdit :workspace_="workspace_"></WorkspaceEdit>
    <WorkspaceDelete :workspace_="workspace_"></WorkspaceDelete>
  </UButtonGroup>
</template>

<script setup lang="ts">
import type IWorkspace from "~/types/workspace";
const open = ref(false);

const workspace = useWorkspaceStore();
const isLoading = ref(false);

defineProps<{
  workspace_: IWorkspace;
}>();

async function setWorkspace(newWorkspace: IWorkspace) {
  isLoading.value = true;
  await workspace.swapWorkspace(newWorkspace);
  isLoading.value = false;
  open.value = false;
}
</script>
