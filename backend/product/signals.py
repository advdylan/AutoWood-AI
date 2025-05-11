from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from product.models import NewProject

import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=NewProject)
def set_default_production_stage(sender, instance,created, **kwargs):
    if created and instance.production_stages.count() == 0:
        ProductionStage = apps.get_model('production', 'ProductionStage')
        try:
            default_stage = ProductionStage.objects.get(stage_name='PRY')
            instance.production_stages.add(default_stage)
            logger.info(f"Default stage 'PRY' added to project {instance.id}")

        except ProductionStage.DoesNotExist:
            logger.warning(f"Error: Default ProductionStage does not exist in product/signals.py")
