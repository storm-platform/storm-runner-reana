# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-job-reana is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from storm_job_reana.modules.reprozip.service.workflow import serial_execution_task


class WorkflowSchedulerStrategy:
    _strategies = {}

    @classmethod
    def register(cls, name, strategy):
        cls._strategies[name] = strategy

    @classmethod
    def exists(cls, name):
        return name in cls._strategies

    @classmethod
    def get_strategy(cls, name):
        if cls.exists(name):
            return cls._strategies[name]
        raise NotImplemented("Strategy not implemented yet.")


WorkflowSchedulerStrategy.register("serial", serial_execution_task)


__all__ = "WorkflowSchedulerStrategy"
