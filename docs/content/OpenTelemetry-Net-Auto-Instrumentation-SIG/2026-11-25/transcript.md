SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-11-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz (Splunk Inc.)** 04:21 Hey, guys.
**Mateusz** 04:31 Hello.
**Eftiquar Shaikh** 04:36 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 04:51 Chris and Zach seems to be offline.
We can wait one more minute for Raj, but I doubt he will be joining.
**Eftiquar Shaikh** 05:17 Startup hooks issue.
Which we deferred.
I think you and Igor had… shared on that one, right? So what was decided?
**Piotr Kiełkowicz (Splunk Inc.)** 05:33 Igor.
Told me that he would like to work on another approach.
of the fix. I do not recall details.
**Igor Kiselev** 05:43 I will… Do it soon enough. I already have a draft.
**Eftiquar Shaikh** 05:51 What's wrong with current approach?
**Igor Kiselev** 05:54 Current approach may result in loading incorrect DLL, under some edge conditions.
From lunch side.
**Eftiquar Shaikh** 06:07 Okay.
Incorrect deal.
**Igor Kiselev** 06:16 Yeah, so in a case when a profiler DLL have not been loaded in an application, it may load Profiler DLL, and in some cases, it may, result in under some configuration, it may result that another instance of Profiler DL will be loaded in application, and that instance will be used to query if it is insolized or not, and it will be failed, because it is not insolized.
So, it's a little bit tricky about how we… what we do with Pinvoke. I will do it a little different, so my current plan would be, a profiler, on a model load, on a meta… on a, model loaded event, for, our, managed code. We'll just rewrite the method, and make it return true, that it is initialized.
Currently, currently our…
**Piotr Kiełkowicz (Splunk Inc.)** 07:16 I guess I'm dropping.
Let me think.
Happy Thanksgiving!
**Eftiquar Shaikh** 07:26 Okay, okay, we'll wait for the review. But is Profiler attached, that call needs to be there?
If that is not there, we have a potential crash. That's all.
**Igor Kiselev** 07:39 It needs to be there, but not…
**Eftiquar Shaikh** 07:42 Yeah, so if we are calling each profiler attached, we will end up loading the profiler data, and that's what you're saying.
Yeah, okay. I see that point. But that ease-attached call is necessary. Without that, we cannot conclude that Profiler is active.
So whatever means we do, we have to have that gate of ease profiler attached.
That, that's all.
**Igor Kiselev** 08:06 In our case, it would be a little bit different, because if, profiler transporters, managed code, it means that it is attached and it's analyzed and working.
**Eftiquar Shaikh** 08:18 In case of Abdi, it is a different story. In case of pure hotel, that's where the problems arise, actually.
In pure hotel, the startup hooks only mode is, significant. In case of Abdi, you cannot restart a hook without loading the profiler, so you can assume that profiler is there. I mean, that's what my comment says. But in case of hotel, the startup hook is a genuine path that can arrive at that.
is hook installed without loading profiler.
And that needs to be tackled. So it is actually pre-existing bug in Pure Hotel.
The hybrid environment of Abdi is fine. It doesn't.
Because it doesn't rely on startup hook to load the instrumentation data.
But I'll be eager to see your change. Sounds interesting to me.
So looks like there's nothing else for us to discuss.
**Igor Kiselev** 09:22 No one else. Yeah.
**Eftiquar Shaikh** 09:25 Cool. Thank you, Igor, for that. I was wondering what approach you are taking. Interesting.
**Rhynier Myburgh** 09:32 Cool, well, have a wonderful Thanksgiving, guys.
**Igor Kiselev** 09:35 And…
**Eftiquar Shaikh** 09:36 You too.
Take care.
Bye.
