# -*- coding: utf-8 -*-
# Imort tools (for updates, etc.) and time (for logging):
import libs.base as base
prop = base.Proportion(self.get_theta(key="Treatment", value=self.action["Treatment"]))
prop.update(self.reward["value"])
self.set_theta(prop, key="Treatment", value=self.action["Treatment"])
