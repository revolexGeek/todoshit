<template>
  <UContainer>
    <UCard class="max-h-dvh overflow-y-auto">
      <template #header>
        <div
          class="flex flex-row items-center flex-wrap gap-[16px] justify-between w-full"
        >
          <div class="flex flex-row items-center gap-[12px] flex-wrap">
            <h1 class="text-xl font-bold">Todoshit</h1>
            <div class="flex flex-row items-center gap-[8px] flex-wrap">
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
              to="https://github.com/revolexGeek/todoshit"
              target="_blank"
              icon="i-heroicons-sparkles-20-solid"
              color="gray"
              variant="ghost"
            ></UButton>
            <Sidebar></Sidebar>
            <ThemeToggle></ThemeToggle>
            <FastCommand></FastCommand>
          </div>
        </div>
      </template>
      <div class="h-auto w-full overflow-y-auto">
        <slot />
      </div>
    </UCard>
  </UContainer>
</template>
