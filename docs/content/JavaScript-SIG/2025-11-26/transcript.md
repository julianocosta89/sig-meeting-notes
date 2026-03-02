SIG: JavaScript SIG
Date: 2025-11-26
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:40 A.
I was trying to catch up and grok that tracing channel stuff.
I think I understand the mechanics, I don't have a good idea of what a better API would be.
Hatto.
**Marc Pichler (Dynatrace)** 01:03 Yeah, that's a bit,
it's a bit frustrating looking at it, because I know, like, how the things would fit together, but coming up with a
good API for it is a different thing.
Especially because we have these bind, things and stuff like that, where you can, like, run stuff with the context,
But it just takes a context as, as an argument.
And…
for tracing channels is always the context that's going to be active when the tracing channel is running, which…
Also makes, kind of, for an awkward, thing there.
Yeah, anyway, hello. No, sorry, I'm…
**Trent Mick** 02:03 been quite excited.
I can't rattle off the context API at all.
Excellent.
Anyway, sorry, ignore me.
**Marc Pichler (Dynatrace)** 02:14 I was just about to say hello, everybody. Let's get started. I'm not sure if there's…
more people that are going to join today, I guess.
folks in the US might be traveling.
for Thanksgiving, so… I guess we can just get started here.
The first topic on the agenda today is my own. I'm looking for somebody to take over
reviews for adding, new instrumentations, because I've…
kind of agreed to do too many things right now, and I probably won't get to it.
Zoom. So, the first one here is…
Instrumentation length chain, and the second one here is,
the instrumentation MCP. I think they're…
I'm not sure if there's another one, that just adds a skeleton, but, yeah, there's…
A bunch of stuff that's, like, vaguely,
Vaguely defined here, and there's also some prob… Some… not problems, but some odd ways of… of…
instrumenting that I saw.
Somewhere around here, can't find it now after DFIS2.
Well, I think it's just using, import in the middle and require in the middle directly, which,
It's kind of a bit different than usual, so it might take some work to figure out what the idea behind these things was and, to do.
how to find a different approach, so if anybody has time,
Please feel free to look into those, yeah.
That's pretty much all for this. And then…
**Marylia Gutierrez** 04:36 for this one. I'm not sure if this is right, because I'm just looking at this now, but there is a proposal for, like, a SIG for MCP.
It was created. We were just discussing this now, but the thing is that
given, like, effort of stabilization, that one might not get accepted, just because we don't have enough, like, GCNCC to look into this. So it's gonna be, like, criteria for each SIG, if they want to add on their own, but I don't think it's necessarily…
there is…
something to align all… how all of them are being made, so just something to keep in mind that…
This might bring extra work for, like, the maintainers.
Keeping in sync with others.
**Trent Mick** 05:24 You said a SIG for… you said a SIG for MCP. You mean there's a PR for semantic conventions for MCP, right? Because there's already a GenAI SIG…
**Marylia Gutierrez** 05:35 So…
**Trent Mick** 05:35 I'm gonna make sure I don't misunderstand you.
**Marylia Gutierrez** 05:38 Because, yeah, I'm just looking at the word MCP, maybe I'm looking… maybe are different things, but I'm talking about…
Can we get the link?
Talking about this one?
**Marc Pichler (Dynatrace)** 06:03 Oh, it's a spec project.
Thing?
Or, like, overall project.
**Trent Mick** 06:24 Interesting.
**Marylia Gutierrez** 06:27 And just, you know, like, there are more people working on it, in case anyone wants to align what the others are doing, but yeah.
**Marc Pichler (Dynatrace)** 06:40 It seems that this is about, MCP servers, actually.
This doesn't seem to be instrumentation, right?
**Marylia Gutierrez** 06:58 I think this has kind of, like, started as…
Specific from the collector, but now they wanted to kind of, like, broad the idea.
**Marc Pichler (Dynatrace)** 07:11 Interesting. Yeah, thanks for bringing that up.
**Marylia Gutierrez** 07:15 Yeah, I don't know nothing about it, I just recognize the names.
**Marc Pichler (Dynatrace)** 07:22 Yeah, I haven't,
I haven't looked into it too much as well, so I probably know less than anyone else here on the call.
So, yeah.
Yeah, thanks for bringing that up. I guess, instrumentation language chain is… Then,
One thing that's… that might be easier to get in than the other one, so…
I'm not sure. As I said, I haven't had much time to look into it, so if anybody has time, I would appreciate you having a look.
That's pretty much our… Hmm.
Alright.
Hmm…
Then, moving on to the next topic, this is just an FYI, the browser-seq now has approver access to our web-targeted packages, both the core and contribute repos.
So…
they are now able to merge PRs that are scoped to these packages, as long as they don't, also modify, things like package log JSON and stuff like that. So, code changes.
should be.
Bit more quick, to get approved there now.
Yes, and…
I guess we can move on to the next one. This is Marillia about a new function for SDK start decision on parameters.
**Marylia Gutierrez** 09:01 Yeah, so this one, yeah, thanks for… for the comments you added there. So this is gonna, like, a push…
a decision on the majority, but I wanted to check people are okay with those decisions. There are just two that I… that I just wrote out that I need to check, like, compatibility, because it exists something under the car config, but I'm not sure if it is, like, a one-to-one situation, so I cannot decide, yet, but…
So yeah, a few of them, we don't need it anymore, like the tech resources or contacts manager, so I just remove, because they're, like, not needed, also for the IG generator, that are the majority of the others, they already exist on the Clarity config.
So, we can probably just remove them, like the log records, metrics reader, and related to traces.
There are only two that, right now, they are tagged as development, even where the name is, like, Instrumentation Development and Resource Detector Development, which seems to be, kind of, like, still changing a little, so I don't think it's safe to…
just rely on that one for now. So I just marked them as, like, okay, keep the programmatic config for now, and eventually, when that gets, like, stabilized, we can then align and probably remove.
But that's kind of the idea, just want to check if people are okay with that.
**Marc Pichler (Dynatrace)** 10:31 Yeah, I don't have any,
like, strong opinions, from the get-go here. Yeah.
one thing that I would note with, things that exist under development and might change is that, if we have this,
Instrumentations config options, and we plan to remove it later on.
It will change for folks regardless.
So…
We might be able to also just use the underdevelopment, variant and, like, have it be a separate…
thing.
From the Node SDK.
Set up stuff.
Which people might keep using until they're ready to switch over.
**Marylia Gutierrez** 11:23 Hmm.
**Marc Pichler (Dynatrace)** 11:23 But it's just… just an idea. It doesn't have to be done… doesn't have to be done that way, it's just something that popped into my mind right now.
**Marylia Gutierrez** 11:35 Oops.
**Marc Pichler (Dynatrace)** 11:41 But I guess this is also a call for people to go on over to the, to the doc and put their comments on there.
**Marylia Gutierrez** 11:49 Yeah, yeah. If anyone, like, does not agree with any of those, yeah.
**Marc Pichler (Dynatrace)** 11:55 Alright, yeah, that sounds good.
I think I do, but it's hard.
**Trent Mick** 12:03 Like, I don't know. Like, I kind of think service names should be in there, but I don't have a good sense of what the uses of this thing are going to be.
Yeah, I don't know. Because it's saying this function to start the SDK is…
Possibly, and maybe this is an issue from second system syndrome, is, like, we want to fix all the things in doing this, and it's not just about declarative config, maybe.
So, like, should this be the entry point for convenience for users to start an SDK?
Whether or not they're using declarative config, and if so, what…
**Marylia Gutierrez** 12:44 So yeah, if they're not using, like, if they're not using the file, the thing…
the function still… the… the backup option is still environment variable, so they can still use service name with two different environment variables they can use today. That doesn't change. This is more like…
The programmatic one is getting removed.
**Marc Pichler (Dynatrace)** 13:10 I think, also, the…
nice thing about the declarative config is, if we want to make it as, like, the default thing that people are going to use, we can provide, like, a
Same defaults, YAML file that we can give folks, that they can use as a starting point.
And then modify as there needs to both, and it would also… yeah.
**Marylia Gutierrez** 13:44 I was gonna say, like, even the specs, they're pretty much the idea from the specs of the client config is, like, what you see here is what you get, but if we are seeing, like, oh, you are putting a server's name there, but then you have the programmatic config with another service name.
And then you see their name, so it's not following this back of what you see is what you get, kind of thing. So this is why, if we have one source of truth, we don't have to make those decisions of priorities.
**Marc Pichler (Dynatrace)** 14:19 And the user also doesn't have to go hunt for where things are being set.
**Marylia Gutierrez** 14:26 Yeah, it's all single source.
**Marc Pichler (Dynatrace)** 14:31 Yeah.
**Trent Mick** 14:41 Okay, sorry, I don't have anything useful to add yet.
**Marc Pichler (Dynatrace)** 14:47 Alright, then I guess, everybody, if you have some time, head on over to the doc, and then we can continue the discussion there.
Yep.
**Marylia Gutierrez** 14:59 So, next one is for one of those specific cases. So, because I was like, okay, remove the resources, but the current case, the default is, for example, if you don't have, like, on the environment, it does have, oh, it didn't tag the right line, but it is just, like, calling, default, yeah.
default resources. So I kept the same behavior, saying, like, okay, if you don't have,
Like, a default resource, use the default, but…
I just want to make sure that if we should still be doing this, because the default is just saying, like, DLTAL SDK is JavaScript, which version? That's pretty much it, what it has on the default. So, I was thinking, should we keep this, have a default, or if I should also
increments the…
the config one, in the sense of that default is always the base, and you just add things on top of it.
**Marc Pichler (Dynatrace)** 16:03 Hmm.
So,
I think here we can just keep using the default resource. I seem to remember that there's some specification for this.
But I'm not sure what the correct way now was anymore. It's one of these things. I think we had this wrong in…
Or the SDKs?
And then we changed it with SDK 2.0, and now it's spec compliant.
So, if it's not.
**Marylia Gutierrez** 16:36 Should I merge?
So, my question is then, should I merge the values?
**Marc Pichler (Dynatrace)** 16:42 I think the spec… was… specifically saying not to merge it,
only if the user doesn't configure anything at all, then I think we should use the… default.
**Marylia Gutierrez** 16:57 Huh.
**Marc Pichler (Dynatrace)** 16:57 So the way it is right now…
**Marylia Gutierrez** 16:59 Okay.
I'm gonna leave them the way it is, right there, then.
**Marc Pichler (Dynatrace)** 17:10 Yeah, I think that's good. There's…
it might be worth double-checking the spec. There might be some place somewhere in the spec, either in the resource or,
tracer provider, or metrics provider, or logger provider spec.
That says what to do with the resources that are associated.
**Trent Mick** 17:33 I just gave a link in chat.
**Marc Pichler (Dynatrace)** 17:35 I think it's the relevance.
Yeah, exactly, this is this. This resource must be associated with a tracer provider or a meter provider if another resource was not explicitly specified.
So I think the code that you have right now is the correct way to do it. So if nobody gives,
default, then…
We must associate it with that, and then we should be okay.
**Marylia Gutierrez** 18:13 Okay.
The next one, just me, just a call for review, because I have two PRs up. The second one is a bunch of errors, because I need the first one to get merged first, because it's solving something that I saw.
And then, once that one is get merged, all the errors from the second will get solved.
**Marc Pichler (Dynatrace)** 18:49 Alright, I guess this is a clerk for review.
**Marylia Gutierrez** 18:51 Yeah, just go for it.
**Marc Pichler (Dynatrace)** 18:55 Alright.
Or try to get to these, that's yeah, sounds good.
Any questions or comments for these PRs?
If not, then,
I have another question, and that is, I've been thinking about the, start node SDK function and how we should deal with experimental packages. You're probably aware of this,
PR…
blog post thing about the changes for stability work, and the idea of having experimental stuff being off by default.
So… That is obviously a breaking change.
would be a breaking change if we were to go in now in the Node SDK and say, you have to opt in to everything.
That's experimental, explicitly, but it wouldn't be a breaking change for the…
start node SDK function, which is new and doesn't have any users yet. So… I'm just wondering if you have any thoughts on… on that.
specific topic.
**Marylia Gutierrez** 20:22 Specific for the new one, or in general?
**Marc Pichler (Dynatrace)** 20:26 In general, for the new one, like, I would say mostly scoped to, like, the start node SDK stuff.
**Marylia Gutierrez** 20:36 Yeah, because I'm thinking, like, the opt-in of this is just you use the function or not.
Right?
**Marc Pichler (Dynatrace)** 20:45 Yes.
So…
**Marylia Gutierrez** 20:47 It's not like… it's not like there is, like, a feature on the existing function that is calling this. This…
If the user wants to use this, they know the experimental, and they have to explicitly use this function.
**Marc Pichler (Dynatrace)** 21:00 So I think that doesn't…
**Marylia Gutierrez** 21:02 conflict with the idea of stabilization? Because a lot of that was because there's a lot of packages that
are not getting, like, maintained and stuff like that, so we want to be very clear about those things. But if the goal of this one is just, like, experimental for now, so people can try it out a little, and that would be, like, the official one, I don't think that is a problem there.
**Marc Pichler (Dynatrace)** 21:29 Yeah, so…
what I'm… So, the reason why I'm bringing this up is, the logs SDK, for example, is not stable yet, right? So, if we say,
start Node SDK, and somebody goes into their declarative config and, like, says, oh, I want to have, like, a logs SDK configured.
They don't know that, like, that specific feature is experimental, and we will always have experimental features that are going to be added there.
So I'm wondering if that's something that we should get started with now, to make sure that there's, like, a consistent experience for people that have to opt in to experimental stuff.
**Marylia Gutierrez** 22:22 I see what you mean.
Haven't thought about that. I'm going to have to think and back.
Because I don't even think we were thinking exactly also about this there.
Because, yeah, the idea is, like, from the classic config perspective, like, if you put it there, this means that you want that feature. But it's not necessarily easy for a person just creating there to know that it's…
experimentally.
So when, yeah, I need to think about a way
So making that more clear or obvious, too.
Users.
**Marc Pichler (Dynatrace)** 22:59 Yeah, just… yeah, I'm… I'm also not entirely sure what the right way to go.
is for this one, just something that, I was thinking about here.
cons…
**Marylia Gutierrez** 23:19 Or maybe that is the thing, like, just mark as stable, the logs… It's happiness.
**Marc Pichler (Dynatrace)** 23:27 Yeah.
**Trent Mick** 23:27 Exporters and all instrumentations are also experimental ratings, so…
**Marylia Gutierrez** 23:33 Come on, friends, stop giving me problems.
Yeah, because, like, one thing that I'm thinking is that, like, if the…
programmatic config, like the SDK options, is a list of, like, opt-ins.
That could be, like, a way for you to be clear.
But, yeah, I don't know, I had to think about it. What is the less weird way to do this?
**Marc Pichler (Dynatrace)** 24:04 Yes.
Alright, yeah, I just wanted to bring it up, so,
Guess we can think about it in the PRs,
That we'll follow, and then we can go from there.
**Marylia Gutierrez** 24:26 Yeah, I can't create an issue just to make sure that we… Don't forget about that.
**Marc Pichler (Dynatrace)** 24:32 Yeah.
Alright.
then I guess we can move on to bug triage. If anybody has any…
Topics you would like to discuss, please feel free to just interrupt me, and then we can go back to discussing topics.
Alright.
So, the first one here is…
V8 panics and excludes plugin from instrumentation. That sounds… Terrible, actually.
Run service A with debugger attached.
the breakpoint.
In instrumentation.js.
This looks… very weird, but I'm not sure if that's something that…
We are causing, necessarily, or if it's just,
some talking V8.
Ran the same steps with node 22 seems to work.
But Express plugin still doesn't respond. I think this person had another issue over at OpenTelemetry.js contrib trip.
I lost it.
This one here.
And it was sorted out, and because they had not… used, below the hook.
So, I guess that was the reason why I didn't see,
be the Express plugin being used.
Hmm.
I guess I can assign this to myself and look into it later, but…
I'd be very surprised if, that's our code.
not necessarily causing this. Might be worth to…
Cut this down to a smaller reproducer and send it, send it upstream somewhere.
Alright, so that's the first one. The second one, I haven't looked into yet. We talked about this last week, I think.
This is… an OTRP transformer issue, where there's a wrong… that there's wrong data exported from the JSON exporter.
Then, I guess we can go on to the next one, which is, instrumentation AWS Lambda breaks.
London Node 24 runtime.
**Trent Mick** 28:41 Opened 7 minutes ago.
**Marc Pichler (Dynatrace)** 28:45 Oh yeah, that's a new one.
**Trent Mick** 28:57 Oh, well.
I haven't cast it.
**Marc Pichler (Dynatrace)** 29:03 Right?
Thanks.
**Trent Mick** 29:08 Sorry, it's a total guest, though.
**Marc Pichler (Dynatrace)** 29:11 I didn't, didn't hear it fully, what you said.
**Trent Mick** 29:16 By the guess of what the issue maybe is.
But again, this is just the minutes ago, so I'm gonna need to take a look, but the… I'm guessing the land instrumentation is…
So it's gotta wrap the user's handler.
I'm guessing the path it chooses to do that is to always transform it into a…
Lambda that uses the callback.
Option.
as Lambda, and not try to keep One that's promise-based.
To be a wrapped, promise-based one.
Heck.
**Marc Pichler (Dynatrace)** 29:54 Yeah, I think I've seen some… Code for this.
Ignore repo.
I guess this is… P1 anyway, because we claim to support this.
Runtime… And… It's causing problems for end users.
And Jonathan is the component owner for this server.
ping him here.
Right, so let's move on to the next one.
This here is Instrumentation Express.
bare middle backend reserve value for HTTP route attribute.
So, they're using… Express 5…
response before the route handler runs.
HB route isn't related with the full matched route.
Yeah, I guess that makes sense, because the way that it's computed is it just…
Stacks on top of each other.
This is P2, and…
instrumentation Express on here.
to all my PR and contribute to fix, so…
I guess I would just,
Let them know that… I'd be happy to see a PR for this. I'm not exactly sure how…
We would do it because this…
essentially returns before the next one runs, so I'm not sure exactly how it would stack these together, but.
**Trent Mick** 33:21 Yeah, I could see this being a sorry, just not supported.
Because it might… Yeah, you know.
The wrap thing determining the route just never gets called, so you'd have to fundamentally… you'd have to make a pretty significant change to the express instrumentation, wouldn't you, so that it's…
Instead of just wrapping the route function to set the route when this gets called, you'd have to…
Look at everything you've wrapped and create your own… Way of determining routes.
Do the route determination before you call any of the handlers, set that information, and then let the handler's system run.
**Marc Pichler (Dynatrace)** 34:02 Yeah.
**Trent Mick** 34:04 Which might get really gross.
Damn.
**Marc Pichler (Dynatrace)** 34:07 I think… I'm not sure what the, HTTP route…
if it's required to be on there, or if HTTP route is only required if you know how to
computed.
I think that… that was the way that it's raised in the…
semantic conventions is somehow that you don't have to set it if you don't know, because there's plenty of situations where you don't know what the route is.
And I think that might be one of these cases here, where instead of, incorrectly setting…
just half the route. We…
Would just not send it at all.
**Trent Mick** 35:03 are… Yeah.
semantic conventions for HTTP span says it's conditionally required if and only if it's available.
So I guess he could argue it's not available here.
**Marc Pichler (Dynatrace)** 35:16 Yeah.
Looks like they also linked another issue here.
It looks like this was already fixed.
Approster system.
I were… Type out the comment after this, I'll let them know that…
Probably the easiest way, that's compliant with semantic conventions is to omit it in these cases.
**Trent Mick** 36:26 Oh, I see what you mean about the partial. Was it already…
**Marc Pichler (Dynatrace)** 36:33 Yeah, it's this year. Because…
**Trent Mick** 36:37 It might also be difficult, given the implementation, but yeah, I see what you'.
**Marc Pichler (Dynatrace)** 36:40 Mmm.
**Trent Mick** 36:41 Oops.
**Marc Pichler (Dynatrace)** 36:43 Yeah, because this is… really confusing, if you see that on the telemetry. There's some,
Some routed that's… Might not even do anything.
So, yeah.
**Trent Mick** 36:59 Yep.
**Marc Pichler (Dynatrace)** 37:01 I'll type up a comment after this, and then,
link to the, SAMConf as well.
Alright.
Guys, let's move on to… PR triage.
This one here hasn't had any activity, so I'm gonna skip it.
Or we could talk about React Native, maybe it's…
I think it's definitely worth talking about this, because this has a lot of,
Thumbs up, and it's something that people are… looking into.
I wonder if we should…
Like, type up a comment or something about the way forward for this,
Right now, the browser sync is… Probably something that's… Kind of a priority, or… Getting a first, usable.
Bing out there.
But once the processing has, kind of, kind of established some…
Way of working in some packages that…
That's being worked on. It might be worth, thinking about.
starting up a similar SIG for, React Native.
That follows a similar pattern.
I'm not sure what your thoughts are about this. I'm not a React Native expert, but,
It feels like it's different enough from browser stuff that it doesn't really fall into the browser stuff category.
So…
**Trent Mick** 38:58 I agree. Maybe we could take off target browser. I may have been the one that added it.
And maybe we could consider adding it, I don't know, it's an instrumentation that… People want, and…
There are two proposed maintainers for it.
**Marc Pichler (Dynatrace)** 39:17 Yeah, one of the difficulties that I've seen with
trying to run these things is that it just adds a lot of dependencies, that…
Make things a bit more difficult to deal with in the repo.
So in a sense, I'm…
**Trent Mick** 39:39 Yeah.
**Marc Pichler (Dynatrace)** 39:40 I think having a different repo for especially these sorts of things makes sense,
Because there, also, the way of working is way different, right? You have,
Your stuff will run things against, android and iOS.
you need to set up a bunch of things in order to be able to run stuff.
Examples and whatnot.
So… It also brings in a lot of boilerplate code.
Which is something to think about.
I guess it's…
In the end, the main reason why this PR didn't go any further is because there's just a bunch of unknowns where we don't know what to do with it.
Go.
**Trent Mick** 40:39 Damn.
**Marc Pichler (Dynatrace)** 40:53 If you want, I can type up, response that's, not specifically for this, PR here, but…
I think it's… yeah, that's the issue in the core repo. It has, like, a bunch of thumbs up here, which is support for React Native environment.
And I would essentially say,
Ideally, we'd figure out a browser first.
And then… once that's somewhat sorted out, think about spinning up, like, React Native.
Think.
Because in the end, the, the,
Android is a different SIG, right? And…
I'm not sure if there's an iOS SIG.
But it seems to kind of fall into a similar category there.
Where it makes sense to have folks that are very into this, app development stuff that,
Know the way around it.
can maintain.
And maintain it.
Or, type something up there, to kind of at least give a status update of, what's going on.
And then, I guess we can…
hopefully move on, and also sort out this PR here. In the process.
**Trent Mick** 42:41 Thank you.
**Marc Pichler (Dynatrace)** 42:45 Alright.
Let's move on to the next one.
I was planning to respond to this and also sort out this,
Same kind of stuff. I'll ping the person here.
And essentially say that…
I guess since this now uses the, what's the cardinal?
the enum from the core repo.
I guess we would have to have another, enum value there. That's…
Latest experimental, so it's not just as easy for them to… Change this up.
**Trent Mick** 43:57 I'm not following.
**Marc Pichler (Dynatrace)** 43:59 Essentially, I think the way that it works is there's this, SAM constability…
**Trent Mick** 44:07 It just takes a string, though, there, so you don't have to change anything.
**Marc Pichler (Dynatrace)** 44:14 Yeah, but it does return the enum.
That's then used to… Check.
Everywhere, I think.
**Trent Mick** 44:26 Karen.
**Marc Pichler (Dynatrace)** 44:28 That's, like,
Not as easy as just changing the string.
But I guess, eventually, the latest,
Latest experimental would morph into becoming the staper… Value anyway, right?
So instead of… Getting the latest experimental string, we would just… change it.
Yeah, that also doesn't work. I need to think about this a bit more and give a proper response here, but…
I also still need to make the same kind of PR,
To add this option to begin with.
**Trent Mick** 45:53 Oh, sorry, another stupid question.
Maybe it's stupid.
like, could we update AMQP? It's… I mean, we could just do a breaking change on instrumentation AMQP, right? And it's kind of potentially a middle finger to people.
Because we're gonna totally change the semantic conventions that it's using, but still not be stable.
So there's no… And, like, potentially not even have a…
A migration path there for people, other than they need to, like, painfully, explicitly in the version.
Yeah, I think that's what we, what was done with, SQS.
**Marc Pichler (Dynatrace)** 46:32 Maybe?
**Trent Mick** 46:34 Sounds right.
Because this was… that was before we were…
Probably even thinking about any opt-in.
Migration process, and… At the time, the semantic conventions it was using were years behind what
Had been moved on, yet not stabilized for messaging.
Yeah.
So, like, I mean, you can argue both ways. I guess the argument I'm making is it's unfortunate that AMQP, just as a matter of timing, is kind of stuck.
In the dark ages of semantic conventions.
and requires… I don't know, heavier lift. I don't know.
I don't know what's best for users.
**Marc Pichler (Dynatrace)** 47:24 Yeah, I guess, at least with the, with the other one that we did, I saw a bunch of users, being bummed out about, not having
The processing spans and stuff like that anymore.
And we're.
**Trent Mick** 47:44 There was the one initiative.
**Marc Pichler (Dynatrace)** 47:45 suspend links.
Yeah, there was this one issue, and I think I've seen in a bunch of other places that people were…
not too happy about not having these anymore.
I guess the spend link support, in…
Various places is also not fully there yet, so…
That's why people are kind of unhappy about this change as well.
**Trent Mick** 48:22 And then messaging is hard enough, and then people move on with their day, and then these PRs just sit there, and…
**Marc Pichler (Dynatrace)** 48:30 Yeah.
Anyway, I will look into…
adding this in as I'm confident. I will look into how we can,
fit that into the existing enum so that I can give them a proper response here on how to go forward with this.
Just having the sort of, back.
Optin to, hey, this is the latest experimental, might help lift new instrumentations, at least to the,
To a status where… It's then easier to…
migrate to the stable semantic conventions once semantic conventions get stable, because then it's not the standstill for old
instrumentations that use the old time count.
Can just update under this flag, and… Not break people immediately.
All right then…
Moving on to the next one.
**Trent Mick** 49:52 Also messaging.
**Marc Pichler (Dynatrace)** 49:56 That's actually context propagation.
That seems like…
I think there was some comment… London…
This was actually a forced push, so… It was 4 days ago.
our… let's… Trying to get back to the person.
here.
I'll leave this open for now.
Then we have…
Langchain, this is what we talked about earlier.
Then we have…
Instrumentation, I already see… I pinged the component on us here, but no response.
This has been sitting for about a month now. More than a month.
Two months.
**Trent Mick** 51:55 I hope to get there sometime, but I don't wanna…
I can't put my name down.
For time.
**Marc Pichler (Dynatrace)** 52:01 Yeah, same. I had looked into, instrumentation IO reads recently,
I just don't know enough about the intenders to…
Commit to reviewing it and actually getting to it in… -Oh.
Reasonable time frame.
Seems fairly straightforward, though. Well, our…
I won't put my name down for this right now, but if I have time, don't worry.
Try to work my… Way to disappear.
And we have, blank chain instrumentation again.
**Trent Mick** 53:09 Looks like there's some recent traffic on that one.
And, Hector, you were doing some review on it?
**Hector Hernandez** 53:16 Yeah, I have been reviewing that one.
I need to take a look at it again, but yeah.
**Trent Mick** 53:22 Yeah, I think there's traffic just yesterday. He did some commits.
**Marc Pichler (Dynatrace)** 53:26 Thanks for, reviewing that one.
Alright, then… I guess we could move on to the next one.
The browser navigation instrumentation, seems like there was a bunch of, activity here, and… Last commits were…
yesterday, so I think this is on track. Nothing to do for us right now.
I think we also need to make sure that,
The new part is then added, to the code owner's file.
I'll just make sure to add them once this PR is merged.
Usually.
Keep up with what goes into the main branch.
Searches react once that happens.
Then we have these two, instrumentation MCPPRs.
And there's another one for the… Responses API.
Yeah, thank you, Hector, for, also reviewing that one. Very much appreciated.
Guess the first one. Untracked, untracked then, and then we can…
Move on to the next one…
Yeah, quick note about the Renovate PRs, they weren't merchable, or…
few months now, because of this bug in NPM, but, I recently changed the config back to use the latest version, because the bug fix was published.
And…
now, if you use 11.63, it should work again. So, shouldn't mess up the package log JSON anymore, and you can…
Go ahead and merge, renovate PRs again. So…
If you stumble upon any of these,
Feel free to go ahead and merge them.
Right. Not this one, though, because this one's failing checks.
Then this one is the next one, which is,
Picking which packages should be compiled and tested.
**Trent Mick** 56:54 Are you stuck waiting for opinions on that, David?
**David Luna Bistuer** 56:59 Yeah, but I'm still looking on, remember that the…
delete the comment, or my next needs a target to…
Actually, you're passing a target, so…
Yeah, as you pointed out, it…
Depends on which target are you trying to run. It returns a different graph.
So I'm still figuring out what's the best way to do it, if we can do it directly with,
to the next, so having everything in packages as an NPM script.
Or having something just for that, just a specific script in the scripts folder, something similar.
**Trent Mick** 57:39 Okay.
Okay.
Would it be reasonable to put this back to draft? And for a while? Yeah.
**David Luna Bistuer** 57:46 I'll do that right now.
**Trent Mick** 57:48 Okay, thanks.
**Marc Pichler (Dynatrace)** 57:50 Alright, thank you.
Alright…
And the next one is also renovate.
And this one here is in draft.
I'm not sure if, Jared was planning to…
Demo folder, browser not ready for review.
Alright.
Looks like everything… work.fine, though, with this PR.
Having that plugin could be helpful.
Not just here, but also in the… in the core repo.
I guess it's failing because there's one instrumentation that's,
Instrumenting something that's not widely available, so…
But since it's just intended as a demo for the other sig, we can leave it there for now.
Alright, looks like we're out of time.
Thank you, everybody, for joining.
And I will see you next week.
**Trent Mick** 59:13 Extra.
**David Luna Bistuer** 59:14 Bye.
**Hector Hernandez** 59:15 Thank you.
**Marc Pichler (Dynatrace)** 59:16 Thank you, bye.
