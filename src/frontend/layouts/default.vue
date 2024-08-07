<template>
  <UContainer>
    <UCard class="max-h-dvh overflow-y-auto">
      <template #header>
        <div
          class="flex flex-row items-center flex-wrap gap-[16px] justify-between w-full"
        >
          <div class="flex flex-row items-center gap-[12px] flex-wrap">
            <NuxtLink href="/" class="text-xl font-bold">Todoshit</NuxtLink>
            <div
              class="flex flex-row items-center gap-[8px] flex-wrap"
              v-if="status === 'authenticated'"
            >
              <UButton
                label="Work"
                size="xs"
                color="black"
                variant="solid"
              ></UButton>
              <UButton
                label="Home"
                size="xs"
                color="gray"
                variant="outline"
              ></UButton>
              <UButton
                label="Todoshit"
                size="xs"
                color="gray"
                variant="outline"
              ></UButton>
              <WorkspaceSettings></WorkspaceSettings>
            </div>
          </div>
          <div class="h-fit gap-[12px] items-center flex flex-row">
            <UButton
              to="/signout"
              color="gray"
              v-if="status === 'authenticated'"
              icon="i-heroicons-link-slash-20-solid"
            ></UButton>
            <UButton
              to="https://github.com/revolexGeek/todoshit"
              target="_blank"
              icon="i-heroicons-sparkles-20-solid"
              color="gray"
              variant="ghost"
            ></UButton>
            <Sidebar></Sidebar>
            <ThemeToggle></ThemeToggle>
            <FastCommand v-if="status === 'authenticated'"></FastCommand>
          </div>
        </div>
      </template>
      <div class="h-auto w-full overflow-y-auto">
        <slot />
      </div>
    </UCard>
  </UContainer>
</template>

<script setup lang="ts">
const { status } = useAuth();
</script>
