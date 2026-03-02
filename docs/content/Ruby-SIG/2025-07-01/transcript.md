SIG: Ruby SIG
Date: 2025-07-01
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/DUXeIjh8qcrXmyiugJ5g82c3FwVhHfm6Kq1dx-za__t9ZMmTk-eWaiaQF5IlCMo.LngRJ7ikU_fhTqcC
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:09 Hi, Hannah!
**Hannah Ramadan** 00:14 Hi, Kayla! How are you?
**Kayla Reopelle** 00:16 I'm doing all right. How are you.
**Hannah Ramadan** 00:18 Good.
**Kayla Reopelle** 00:19 Good.
Okay, I can share my screen.
Okay? So at the spec Sig today.
it was kind of a short meeting, but there were some additional concerns raised around
oops. Not this one.
Well, maybe it didn't get added as a link, but around the extended attribute value types.
It sounds like Js. Is concerned about how they would integrate them, and
the change feels kind of vague. So I think there's still a ways to go in terms of discussion before that one gets merged in.
Everything else didn't seem immediately available
or like, I'm sorry, applicable to us.
so yeah. So there isn't really anything else I would report back from that meeting today.
as far as core goes, I guess. Does anyone have anything that they want to talk about today before we just start going through each of the repos.
**Hannah Ramadan** 03:09 Nothing for me! No.
**Kayla Reopelle** 03:11 Okay.
**Xuan Cao** 03:15 For the dynamics. SDK.
**Kayla Reopelle** 03:20 Yeah, yeah, we can, we can definitely do that.
**Xuan Cao** 03:23 Okay. Thank you.
**Kayla Reopelle** 03:25 Yeah.
yeah, thanks for finding that that bug with the symbols.
So I saw before this meeting that
you pushed a change to the Async metrics. But I didn't get a chance to see what it was.
Was it just that comment?
Yeah, I just I made that suggestion cool sounds good.
What do you think about adding this into the change for the release today? Does that feel? Would you rather have the fix be separate from this new feature, or
or bring them together.
**Xuan Cao** 04:13 Oh, I don't have a secretaries.
this one can. Yeah, this one can make a little bit.
**Kayla Reopelle** 04:20 Cool.
We can do that.
The I did find another potential bug while I was experimenting with the metrics. SDK, this week, when
So when you have a histogram with a view the
Metric store will try to, we'll still create metrics that have empty data points. And I think we've run into a problem before with empty data points.
But the reason why our previous checks for empty don't really solve the problem here is that with the view.
and maybe also without the view, like all the other information about the instrument, is getting created. So you have all of the basic attributes and the resource and things like that. So it's not really empty. But if you try to export via Otlp an error that, or a metric that doesn't have any data points. This is the error that comes up. And it sounds like in the
data model, like the protobuf. You have to have data points. But I wasn't entirely sure
if that's the right call with the spec, and like, perhaps some
instruments are different than others.
yeah. So this is. This is a proposal to kind of fix that error, because otherwise, you know that error shows up at every export interval. Whenever you know that metric hasn't been invoked.
And this seems to solve the problem. If you in the metric stream, you know, kind of stop attempting to aggregate metric data, if the data points are empty.
there's some new tests for it. But but yeah, I guess, Sean, from your understanding with the spec.
like, what? And it's okay, if you can't answer those now. But
do you think it makes sense
to not send metric data? If there aren't any data points? Or do we need to find a way to try to send metric data, anyway, if there aren't data points.
**Xuan Cao** 06:38 Oh, I think we shouldn't send data when there's no data in the data point.
**Kayla Reopelle** 06:42 Okay.
**Xuan Cao** 06:43 Sure.
**Kayla Reopelle** 06:44 Cool. Alright then I will officially open this for review. I needed to change this test a little bit.
because the after the sleep 8. That second snapshot was empty. So I just added a little more data to the second snapshot, so that we could add assertions for it, and it would pass.
So yeah, so I'll open this guy up.
Take a look when you can.
you can also put this in its own release that's separate. I don't think this needs to block the
the fix that you submitted earlier this week.
There's also one other small Pr
related to changing the logs. Exporter default. So when this code was 1st merged, the configurator patch was 1st merged. We didn't have the Otlp exporter released. Yet, so the default was console, but in the specification the default should be Otlp, and since we have an Otlp exporter, I thought it was time to to make that switch.
So that's just the second small one. I guess I'll put
Put these links in the notes.
This one.
okay, let's see, did we have any new issues this week?
Nope, cool. Alright, I think that takes care
of this one. I am surprised that the
release wasn't automatically created since. Oh, it did attempt it.
Oh, gosh, okay. So I think I'm gonna
need to take out that logs. SDK test. That's been flaky.
I wonder if I can re just rerun it, and if it will create it
alright, we'll keep an eye on that.
cool. Alright, let's hop into contribute.
We've had quite a few Prs from
open telemetry bot, and some of the the Gc.
The Gc. Crew just around preparing our repositories for open telemetry to graduate to a full Cncf project out of its incubating project phase. So that's kind of if you see some small changes with the readme, that's what's going on there.
This one, though I don't remember talking about.
Oh, I see. Okay, so it's adding some
permissions for the token usage. This might take a little more time to review, but if anyone is interested in reviewing it and verifying things
that would be great otherwise just get to it eventually.
Hannah, is there anything you wanted to
update on with the semantic convention stuff? How's that going.
**Hannah Ramadan** 11:31 I haven't been able to work on it as much as I would have liked this past week.
I think there's still the Pr. Open that changes the span name for the Http library.
**Kayla Reopelle** 11:42 Yeah.
**Hannah Ramadan** 11:43 So that one would be.
I'd love to get that one merge. Just cause. I think right now we're kind of not really
doing what we're supposed to.
**Kayla Reopelle** 11:51 Yeah.
**Hannah Ramadan** 11:52 Library.
**Kayla Reopelle** 11:53 I think you are totally right. I will
get that merged in and released today.
**Hannah Ramadan** 12:02 You'll need to unlock your iphone first.st
**Kayla Reopelle** 12:05 I'll make sure to do that before I release.
**Hannah Ramadan** 12:09 Perfect. Thank you.
**Kayla Reopelle** 12:13 Cool. So let's see what else is going on here.
alright! Some more of the simcom stability migration.
Oh, this is something
I'm curious about testing, but it sounds like Ariel may have tested it before, and things didn't exactly work.
But there's this open telemetry bot, Github Token, that's available.
that is supposed to be a personal access token compared to the standard Github token.
which might just be called Github token. It may have a slightly different name. But the benefits of a personal access token is that if you're trying to run an action that has other actions, that kind of depend on it, or could that could be triggered by it? For example, if one action creates a pull request, if you are authenticating with a Github Token, those related actions won't run. So when we create new releases right now, we just see
All of you know, we see a couple of workflows run. But the full Ci with tests and all the different gems, doesn't we have to push up an update commit?
And theoretically this would solve the problem.
It it seems to be used in some of the other
repositories for the other Sigs. But I have a hard time figuring out if that's exactly
what it's used for, or what it's solving. But if this is
an experiment you are open to trying out. Please review
review this, I guess, even if you're not interested in trying it out, you can
decline and and and tell me so.
But since it was stale, I thought I'd just bring it up again.
Okay, I think that's it.
unless anyone else has any other questions they want to discuss.
I may not be here next week. I'm gonna be at rails. Comp, and so I don't.
I don't know if this will necessarily fit into my schedule.
So I just wanted to give a heads up on that, but would be happy to meet asynchronously if it doesn't.
**Hannah Ramadan** 15:00 Oh, yeah, that sounds good.
Rails. Comp is exciting.
**Kayla Reopelle** 15:03 Yeah, yeah. Last one. We'll see how it goes.
**Hannah Ramadan** 15:07 Great.
**Xuan Cao** 15:11 Cool, cool.
And so you're gonna give like bookshelf.
**Kayla Reopelle** 15:16 I am. Yes, yeah, I'm given an open telemetry workshop.
and yeah, the plan is to basically just go through
each of the different signals, and how you can add them to your rails, application and their benefits.
You know the the addition themselves is is pretty simple, but I hope, adding more context about why it's important and and how things are working will be valuable to people.
so yeah, are you? Are you going to rails? Comp. Siobhan?
**Xuan Cao** 15:51 No, I
I was searching for a ruby comp this year that I I just saw, and as as
one when I saw that is too late.
And then, yeah, since my
my uncle is living in Philadelphia.
That was.
**Kayla Reopelle** 16:09 I was thinking, if I can go just visiting him.
**Xuan Cao** 16:12 Oh, yeah, yeah.
But yeah, can't. Can't go.
**Kayla Reopelle** 16:16 Bummer, bummer.
**Xuan Cao** 16:17 Yeah.
**Kayla Reopelle** 16:18 One.
Well, at some conference. Someday we'll be able to meet.
**Xuan Cao** 16:24 Yeah.
**Kayla Reopelle** 16:34 Great well, cool. Well, I hope you all have a great great week, and if I don't see you next week I'll see you all the week after.
**Hannah Ramadan** 16:44 Amazing. Thank you.
**Kayla Reopelle** 16:45 Yeah, thank you. Take care.
**Xuan Cao** 16:47 Bye.
**Hannah Ramadan** 16:48 Bye.
