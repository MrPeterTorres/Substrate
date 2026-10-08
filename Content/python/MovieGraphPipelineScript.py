import unreal

@unreal.uclass()
class ShadowCatcherColorLock(unreal.MovieGraphScriptBase):

    PROPERTY_NAME = "bSuppressColorFlicker"

    def _get_fire_light(self):
        current_world = unreal.MovieGraphLibrary.get_current_play_world()
        if not current_world:
            unreal.log_warning("ShadowCatcherColorLock: no active play world")
            return None
        return unreal.GameplayStatics.get_actor_of_class(current_world, unreal.load_class(None, "/Game/Blueprints/BP_FireLight.BP_FireLight_C"))

    @unreal.ufunction(override=True)
    def on_job_start(self, in_job_copy):
        fire_light = self._get_fire_light()
        if fire_light:
            fire_light.set_editor_property(self.PROPERTY_NAME, True)
        else:
            unreal.log_warning("ShadowCatcherColorLock: BP_FireLight not found in play world")

    @unreal.ufunction(override=True)
    def on_shot_finished(self, in_job_copy, in_shot_copy, in_output_data):
        fire_light = self._get_fire_light()
        if fire_light:
            fire_light.set_editor_property(self.PROPERTY_NAME, False)

    @unreal.ufunction(override=True)
    def on_job_finished(self, in_job_copy, in_output_data):
        fire_light = self._get_fire_light()
        if fire_light:
            fire_light.set_editor_property(self.PROPERTY_NAME, False)