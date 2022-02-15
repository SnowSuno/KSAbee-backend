from tortoise import models, fields

from app.common.choices import Position, Tier
from app.common.validators import EnumValidator

from .student import Student


class Account(models.Model):
    id = fields.CharField(pk=True, max_length=50)
    nickname = fields.CharField(max_length=30)
    profile_image = fields.CharField(max_length=256)
    level = fields.IntField()
    position = fields.CharField(max_length=3, validators=[EnumValidator(Position)])
    tier_class = fields.CharField(max_length=20, validators=[EnumValidator(Tier)], default=Tier.UNRANKED.value)
    division = fields.IntField(default=0)
    league_points = fields.IntField(default=0)
    wins = fields.IntField()
    losses = fields.IntField()

    owner: fields.OneToOneRelation[Student] = fields.OneToOneField(
        "models.Student", related_name="account", on_delete=fields.CASCADE)

    @property
    def tier(self):
        tier = self.tier_class[0] + self.tier_class[1:].lower()
        if self.tier_class not in [Tier.UNRANKED, Tier.CHALLENGER]:
            tier += f" {self.division}"
        return tier

    @property
    def key(self):
        return 0

    @property
    def win_rate(self):
        return self.wins * 100 // (self.losses + self.wins) \
            if self.wins > 0 else 0

    async def renew(self):
        pass

