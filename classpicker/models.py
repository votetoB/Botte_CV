from django.db import models


class HearthstoneClass(models.Model):
    title = models.CharField(max_length=7)

    def __str__(self):
        return self.title


class PickUser(models.Model):
    battle_tag = models.CharField(max_length=100)
    choices = models.ManyToManyField(HearthstoneClass)
    finished = models.BooleanField(default=False)


class Pick(models.Model):
    first_user = models.ForeignKey(PickUser, related_name='first_user')
    second_user = models.ForeignKey(PickUser, related_name='second_user')



# class Pick(models.Model):
#     picks_first = models.BooleanField(default=True)  # If False - then bans first
#     no_bans = models.BooleanField(default=True)
#
#     first_picks_finished = models.BooleanField(default=False)
#     first_bans_finished = models.BooleanField(default=False)
#     second_picks_finished = models.BooleanField(default=False)
#     second_bans_finished = models.BooleanField(default=False)
#
#     first_has_paladin = models.BooleanField(default=False, verbose_name='Pick paladin')
#     first_has_mage = models.BooleanField(default=False, verbose_name='Pick mage')
#     first_has_warrior = models.BooleanField(default=False, verbose_name='Pick warrior')
#     first_has_shaman = models.BooleanField(default=False, verbose_name='Pick shaman')
#     first_has_priest = models.BooleanField(default=False, verbose_name='Pick priest')
#     first_has_rogue = models.BooleanField(default=False, verbose_name='Pick rogue')
#     first_has_hunter = models.BooleanField(default=False, verbose_name='Pick hunter')
#     first_has_warlock = models.BooleanField(default=False, verbose_name='Pick warlock')
#     first_has_druid = models.BooleanField(default=False, verbose_name='Pick druid')
#
#     first_bans_paladin = models.BooleanField(default=False, verbose_name='Ban paladin')
#     first_bans_mage = models.BooleanField(default=False, verbose_name='Ban mage')
#     first_bans_warrior = models.BooleanField(default=False, verbose_name='Ban warrior')
#     first_bans_shaman = models.BooleanField(default=False, verbose_name='Ban shaman')
#     first_bans_priest = models.BooleanField(default=False, verbose_name='Ban priest')
#     first_bans_rogue = models.BooleanField(default=False, verbose_name='Ban rogue')
#     first_bans_hunter = models.BooleanField(default=False, verbose_name='Ban hunter')
#     first_bans_warlock = models.BooleanField(default=False, verbose_name='Ban warlock')
#     first_bans_druid = models.BooleanField(default=False, verbose_name='Ban druid')
#
#     second_has_paladin = models.BooleanField(default=False, verbose_name='Pick paladin')
#     second_has_mage = models.BooleanField(default=False, verbose_name='Pick mage')
#     second_has_warrior = models.BooleanField(default=False, verbose_name='Pick warrior')
#     second_has_shaman = models.BooleanField(default=False, verbose_name='Pick shaman')
#     second_has_priest = models.BooleanField(default=False, verbose_name='Pick priest')
#     second_has_rogue = models.BooleanField(default=False, verbose_name='Pick rogue')
#     second_has_hunter = models.BooleanField(default=False, verbose_name='Pick hunter')
#     second_has_warlock = models.BooleanField(default=False, verbose_name='Pick warlock')
#     second_has_druid = models.BooleanField(default=False, verbose_name='Pick druid')
#
#     second_bans_paladin = models.BooleanField(default=False, verbose_name='Ban paladin')
#     second_bans_mage = models.BooleanField(default=False, verbose_name='Ban mage')
#     second_bans_warrior = models.BooleanField(default=False, verbose_name='Ban warrior')
#     second_bans_shaman = models.BooleanField(default=False, verbose_name='Ban shaman')
#     second_bans_priest = models.BooleanField(default=False, verbose_name='Ban priest')
#     second_bans_rogue = models.BooleanField(default=False, verbose_name='Ban rogue')
#     second_bans_hunter = models.BooleanField(default=False, verbose_name='Ban hunter')
#     second_bans_warlock = models.BooleanField(default=False, verbose_name='Ban warlock')
#     second_bans_druid = models.BooleanField(default=False, verbose_name='Ban druid')



# class HearthstoneClass(models.Model):
#     PALADIN = 'PA'
#     WARRIOR = 'WA'
#     SHAMAN = 'SH'
#     MAGE = 'MA'
#     PRIEST = 'PR'
#     ROGUE = 'RO'
#     HUNTER = 'HU'
#     WARLOCK = 'WL'
#     DRUID = 'DR'
#
#     CLASS_NAMES = (
#         (PALADIN, 'Paladin'),
#         (WARRIOR, 'Warrior'),
#         (SHAMAN, 'Shaman'),
#         (MAGE, 'Mage'),
#         (PRIEST, 'Priest'),
#         (ROGUE, 'Rogue'),
#         (HUNTER, 'Hunter'),
#         (WARLOCK, 'Warlock'),
#         (DRUID, 'Druid'),
#     )
#
#     name = models.CharField(max_length=2, choices=CLASS_NAMES)
#     owner = models.ForeignKey('Pick')
