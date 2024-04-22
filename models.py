from django.db import models
from mysql.connector import connect, DatabaseError, InterfaceError


class items(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(null=True, blank=True)
    fling_effect_id = models.IntegerField(null=True, blank=True)

class egg_groups(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    region_id = models.IntegerField(null=True, blank=True)
    identifier = models.CharField(max_length=79)


class moves(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(null=True, blank=True)
    pp = models.SmallIntegerField(null=True, blank=True)
    accuracy = models.SmallIntegerField(null=True, blank=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(null=True, blank=True)
    contest_type_id = models.IntegerField(null=True, blank=True)
    contest_effect_id = models.IntegerField(null=True, blank=True)
    super_contest_effect_id = models.IntegerField(null=True, blank=True)

class pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(null=True, blank=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

class pokemon_form_generations(models.Model):
    pokemon_form_id = models.IntegerField(primary_key=True)
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

class pokemon_moves(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(null=True, blank=True)

class pokemon_stats(models.Model):
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()

class pokemon_types(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()

class stats(models.Model):
    id = models.AutoField(primary_key=True)
    damage_class_id = models.IntegerField(null=True, blank=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.BooleanField()
    game_index = models.IntegerField(null=True, blank=True)

class types(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(null=True, blank=True)
