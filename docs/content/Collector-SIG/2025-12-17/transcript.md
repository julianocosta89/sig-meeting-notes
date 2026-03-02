SIG: Collector SIG
Date: 2025-12-17
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Sam DeHaan** 01:37 Hello, stranger.
**Andy Keller** 01:45 Hey, how's it going?
Sorry, I'm walking back with my food.
**Sam DeHaan** 01:51 I would love to do that, how are you?
**Andy Keller** 01:53 Yes!
**Sam DeHaan** 03:21 Is, anyone else able to access the meeting notes?
That are shared in the, the meeting? I'm getting a strange… Error.
**Mikołaj Świątek** 03:33 Yeah, same here.
Okay. The, the one in chat box.
**Sam DeHaan** 03:42 Fame.
**Jade Guiton** 03:43 Yeah, there's been a migration to a new dock, and I think the old dock was supposed to have a link to the new one, but it was accidentally restricted.
**Andrzej Stencel** 06:35 We should probably get started, right?
Anybody wants to talk about the first topic?
Looks like nobody.
Mmm.
Let me show.
**Jade Guiton** 06:48 Yeah, that's crazy.
**Andrzej Stencel** 06:49 Yep.
**Jade Guiton** 06:51 Yeah, I guess the question is, are there any updates regarding component stability?
**Andrzej Stencel** 07:01 I don't have any updates.
**Tyler Helmuth** 07:10 Andre, do you have access to the Google Doc? I can't open it.
**Evan Bradley** 07:15 They changed to a new dock.
**Andrzej Stencel** 07:17 Yeah, the one in the chat, the link in the chat.
**Tyler Helmuth** 07:19 Thanks.
**Andrzej Stencel** 07:21 Yeah, it sucks.
So the meeting invitation needs to be updated, right? The new link.
**Jade Guiton** 07:36 It hasn't been updated yet, I don't know who has the rights to do that.
**Andrzej Stencel** 07:45 I know Trasko's mentioned somewhere on Slack about this, but I'll follow up and check it.
Trask definitely knows what to do with this.
Excellent.
Okay, I guess if there are no,
Discussion, if there's no discussion needed.
For the stability issues, then we can move on to the next topic.
**Trent Vigar** 08:12 Yeah.
**Andrzej Stencel** 08:12 Andrew, maybe… sorry, Andrew, just to respond into your chat, maybe just add your topic to the agenda regularly.
Wait, how about that?
Oh, it's a kid. Okay, Jen.
**Trent Vigar** 08:26 Yeah, sure.
Looks like we've got a couple of agenda items, so hopefully this one won't take too…
terribly long, but, I started a thread, I think it was in the OpAMP channel, asking about…
People wanting to support Electric config updates through the op-amp extension, rather than the supervisor pattern.
I started off kind of a spike, messing around with the supervisor, pattern and got that to work, but
there's Some… some things with the supervisor approach that won't work for
for me, and what I'm trying to do, so I'm trying to figure out how to…
maybe make some changes to support this with the op-amp extension or something similar, where we can send events to…
To update the config directly in the collector.
The thread got, you know, pretty big, and a lot of people had some thoughts and… and various information that they were…
Talking about ways that they attempted it.
And weren't able to get it to work. So I just wanted to kind of open this up here. I just…
wanted to say that I've spent the past few days trying to do some research and deep diving into the OpAMP extension and the collector code itself. I don't have deep knowledge of all the components, I'm really just trying to learn right now.
And right now, I think where I'm at is just a naive approach instead of trying to…
update config and the collector with the op-amp extension. I'm gonna use the op-amp extension to receive updates to…
send a SIG up to restart the collector, and the collector would use, like, an HTTP config provider to pull config when it starts up again, that's been updated.
But, yeah, I just wanted to open it up, because a couple of you are here, commented about some various approaches that
You were trying to figure out, but for some reason or another, weren't able to get it to work, so…
Yeah, where's everyone at with that?
**Evan Bradley** 10:38 So, thanks for bringing it to this meeting. This is something I think we've been kind of looking at for a long time, but don't really have… there's just… there's so much work that would need to go into…
And I think we've made some progress on it, but there's a lot of work that would need to go into making this work within the collector's framework.
Ultimately, I think that… Doing this inside of the extension?
And Andy might have some more insights here. Might be possible, but I think, ultimately, any solution that only uses the extension and not a new op-amp confMap provider will kind of end up being a hack.
But I think… for…
For the short term, it might be best to either throw something in the extension behind a feature gate, or an alternate extension, knowing that it would be deprecated, but I think the… the biggest, or the…
Excuse me, the most difficult
aspect of this, I think, will be making it so that you can configure compat providers. It's kind of a weird thing, because…
You… the providers are the thing that provide the configuration, but you also want to configure the things that provide the configuration, so you kind of have a weird…
Kind of recursive, loop there.
It is possible, we've discussed it. I can point you to some docs on kind of how we think that might work, but I think that's gonna be the most difficult thing to do. If we are able to make that work, I think that the…
some of the work that Tyler
did, for that POC, is a pretty good start, and would…
Would be a good… would be the, in my opinion, the… the best next step for, trying to make it so that you can accept configuration from an op-amp server within the collector.
I'm reading your comment now, Tyler, but Jad, I see that you have your hand up.
**Jade Guiton** 12:40 Yeah, so I haven't read through the entire thread, I, talked, talked in it briefly, but I didn't read the entire thing, and I was wondering if you talked about what issues you were having with the supervisor, because I feel like…
If we try to really come up with a robust solution.
Within the collector, it's probably gonna look like a supervisor light.
Maybe just a supervisor that's, like, instantiated?
From the collector? So I'm wondering if such a solution would have the same, would pose the same issues for you.
As the current supervisor does.
**Tyler Helmuth** 13:23 I can share one downside that I've experienced with the supervisor recently, that getting to, like, this other type of pattern would solve, so…
The supervisor is itself a client and a server in the op-amp paradigm, so it is a client to the real op-amp server that you're communicating to, it is a server for the collector, and the op-amp extension is a client to the op-amp supervisor.
Yeah, normally this isn't that big of a deal, but what the problems that I have experienced are when,
trying to get… trying to configure the op-amp supervisor via the server. So, like, there are features in OpAMP, like report on metrics, report on traces, report on logs.
And I guess, to a lesser extent, remote config.
Where right now, the op-amp supervisor passes those… Messages straight on to the…
to its client, to the collector, essentially. So, like, if your op-amp server tells the op-amp supervisor, hey, update your telemetry settings to be X, Y, and Z, then the op-amp supervisor says okay, and it tells the collector to do that.
It turns out it's actually kind of annoyingly difficult to…
to get the op-amp supervisor to…
Take those settings and apply it to itself.
And if you wanted the op-amp supervisor and the collector to have different telemetry settings, whether that's different keys, or a different destination, a different URL or something, different headers of some kind.
That is very hard, and I think it would require a custom message.
And that's because the pattern right now is for the op-amp supervisor to try to pass through as much as it possibly can to the collector. So if we had something like an op-amp provider, or… I guess if we just didn't have the supervisor being in the middle, I think that
that problem wouldn't exist. I wouldn't have to worry about trying to configure this additional piece of software, with OffAMP.
**Jade Guiton** 15:31 I don't… Oh.
**Evan Bradley** 15:34 No, Jad, you can go ahead, yeah, you can go ahead, and I have something to ask about that, though.
**Jade Guiton** 15:40 Yeah, I just wanted to react by saying that it sounds like that's not really an issue with…
The supervisor being outside of the collector itself, and more with the current implementation of the supervisor.
As a proxy for the extension, essentially.
**Tyler Helmuth** 15:57 Yeah.
**Jade Guiton** 15:58 Right.
**Tyler Helmuth** 15:59 But whether it's inside or outside.
the problem is, it's a proxy, but it's its own process, so it produces its own telemetry that I'm interested in.
If everything was just inside the collector, if there was an op-amp provider and an op-amp extension or something, then I wouldn't need to feel like I need to configure two different OpenTelemetry SDKs.
And there's precedence for that, so, like, I've seen op-amp
Implementations with the collector, where the entire collector is wrapped
by an op-amp client, and instead of being managed via a sub-process, like an actual executable that's running on the machine, it's… it's managed almost the same way as the hotel coal collector manages the service, where it can, like, shut it down, recreate it, and restart it.
And so that's, like, something that's outside the collector, but it's all still in one sub… one process, so it all has the same SDK, and therefore it can… it doesn't have to try to differentiate
If an incoming message is for me, or for the thing I'm managing.
**Jade Guiton** 17:07 But then it… that limits the options for configuration, right, in the same way you're talking about.
**Tyler Helmuth** 17:14 Oh my god.
**Jade Guiton** 17:14 The process can hardly configure itself or replace itself in binary, right?
**Tyler Helmuth** 17:19 Well, that's what you lose. You lose the ability to replace the binary, but you don't lose the ability to configure, because the remote message can send in different configs in that map, and so that one's okay. But yes, the supervisor exists because it's the only way to replace the binary.
**Jade Guiton** 17:36 I see.
**Evan Bradley** 17:38 So, I guess a couple points on that. First, are you… so you're looking to configure the OTEL SDK in the supervisor through OPAMP? Is that the…
Because my, my, like…
thought, and, you know, others can chime in here, is that the supervisor really isn't intended to be itself configured through op-amp. It's really just supposed to be, like, a thin layer.
**Tyler Helmuth** 18:00 Correct, I agree.
**Evan Bradley** 18:02 of initial options, and then everything else is op-amp below that.
**Tyler Helmuth** 18:05 I agree, that's 100% the intention.
In practice, I have run into a situation where it's like, wow, I really wish I could inject a key into the headers of the op-amp telemetry so that I can get them to go somewhere automatically.
But because of what you just said, that's quite hard, because the op… you're not really supposed to be configuring the supervisor with op-amp.
But it turns out that I want to, because I'm trying to, like, pass config to all of my agents, and it turns out the op-amp supervisor ends up being like an agent when it's being managed by the…
by a server.
**Evan Bradley** 18:42 So, I think the answer… my… er, my gut answer to that would be its own rabbit hole, which would be that the Go SDK should have op-amp configurability.
And then you can configure the supervisor's SDK to do that for you.
Obviously, that's its own, set of challenges. The…
Oh, I'm forgetting the sec- I'm sorry, I'm forgetting the second question I had.
Oh, around upgrades. I think that the thing that you're talking about, which is…
replace the… our, like, hotel call, like, package, that man… that does basically, like, the process management for the collector.
and have that speak cop-amp. My understanding is that's how BindPlane's distro works. And they have, Andy or Dakota can speak better to this, but they have, the ability to do upgrades within their distro, so I don't think we would necessarily need the supervisor for that.
But, they end up, from what I understand, needing a…
They have, like, an upgrade helper that comes with the distro that can do that sort of thing with them, or for them.
**AK Andy Keller** 19:50 Yeah, I can just speak to that really quickly. It was an updater binary that gets executed that, moves over the existing package.
Adds a new one.
Make sure it works. If it doesn't…
It restores the old one.
And that's actually one of the biggest issues, I think, right now with a couple different
approaches to trying to do this with an extension or a config provider is that…
Currently, the collector is just going to shut down if…
It receives bad config, and it's really important that the…
that when OpAMP receives config and tries to apply it to the collector, that it can revert to the previous config if that config is bad.
And so, that's currently what the supervisor does.
And there doesn't appear to be a hook right now to be able to do that kind of thing with the collector.
And I think that's a real barrier to this sort of approach, and… Would be really helpful.
One other thing I'll just… Speak to real quick is,
Why this is interesting to us.
The supervisor just introduces some… a different deployment pattern of a different binary, you know, potentially a different package, and so for…
On… onboarding existing… Users of OTEL,
and they want to have their collector managed, it would be really nice if you just say, like.
you know, change your config to add the op-amp extension, add this URL for the…
management platform, and you're good to go. Instead, it's, you know, change your deployment pattern to use a supervisor instead, and it creates a lot of extra friction.
So, it would be nice to try to find a solution to this.
I see there are a lot of hands up, so…
Go ahead. I'm not sure of the order, but Evan?
**Evan Bradley** 21:47 No, Mikolai, you're first.
**AK Andy Keller** 21:49 Thanks.
**Mikołaj Świątek** 21:50 and… I just wanted to say that
Then the idea of making the collector, perhaps under some configuration option or some such, be a bit more permissive about what it does if it encounters bad config is useful in the supervisor version as well.
Not just in the normal version. Like, for example, it would be very, very nice if you push invited config to the collector, it keeps running, even if it just keeps running and does nothing, and just waits for a new config that would already make some scenarios easier to manage.
If it doesn't exit, and if it could keep running and, for example, only have extensions running without any pipelines, that would be even nicer, because you could then have some level of, state reporting in there.
That's the only thing I had.
**Evan Bradley** 22:46 So, no, that's a good transition into what I was gonna say as well, which is that we have discussed it, I think Trent linked to it in the thread, or somebody did in the big…
discussion that we had, but I think that that would be something that is, I think generally agreed that we should offer as a config option, but we don't want to do it by default just because, that introduces issues of its own.
But if we had the ability to conf…
Yes, probably configure Comp AMP providers, although I think that the op-amp provider might just be able to do this out of the box. We could easily, offer an API that would allow the collector to stay up if it got configures, and it knows that the… or maybe not knows, but if it got configures.
And then, the providers could resubmit new config once they had a valid, config that they, they got. I think we would need to discuss the API, but I definitely think that there's, there's room for that, and I don't think it would be…
that huge of an effort. Don't quote me on that, but still. I do think it's definitely possible to keep the collector up and not have it go down, after it gets an error.
Tyler, you had your hand… oh,
Okay, Tyler, you had your hand up after me.
I just want to make sure that we're not running over too much here. I think we're good.
**Tyler Helmuth** 24:04 Yeah, I don't wanna… I guess I don't wanna talk too much more on the possible solutions, but as we're ideating, I do want to throw out the idea of…
Instead… what if instead of this being in the extension, or this being in…
a custom provider. Is there a world in which
Hotel Cole, the, like, the thing wrapping the service.
has… op-amp.
capabilities, the ability to be an OpAMP client.
And when it receives config, it can restart the service, in… what is it? OTelcool.run, or collector.run, or whatever that is.
Like, I… it would be pretty… I'm wondering if that would be similar to the supervisor… But…
not need a sub-process, and then that could… that would be, like… it'd be really cool if, like.
the collector, like, upstream distributions of our collector, our version of the collector was just, like, op-amp capable.
And you just, like, flip some switch, and then all of a sudden, you've got, like, an OpAmp client running that knows how to manage the collector. Like, thinking about the way Andy was like, we just want customers to be able to use OpAmp with
their collectors, like, it would be pretty cool if it was in Otel Cole, so… I don't know, maybe there's a… a spike to be done there as well.
**Evan Bradley** 25:25 I think… so, we discussed this at the OpAMP SIG meeting last week, and I think there is… the only thing that I said is that it needs to be isolated and easy to turn off, because I could imagine a lot of people getting really queasy if that's just something that's…
**Tyler Helmuth** 25:37 Yeah, it would be an option. Yeah.
**Evan Bradley** 25:42 Trent?
**Trent Vigar** 25:44 Yeah, so…
What we're… what we're talking about as bad config, do we consider that to mean, like, the…
the collector tries to start with that config, and one of the components, is timing out, or… or something like that. Like, just any of the components can't do their normal bootstrapping, and then the whole collector shuts down, is that what we're talking about?
**Evan Bradley** 26:08 Right.
**Mikołaj Świątek** 26:10 That the components can't start, like, if they start and then, you know, report permanent failure status, that's fine, right?
**Trent Vigar** 26:18 Is there such a component where we're not…
Where we're okay with, you know, a timeout trying to do something, or is, like, every single component considered critical to the collector starting up?
**Evan Bradley** 26:30 In general, yes. So, we take, like, a fast failure approach, or fast feedback, however you want to call it. Basically, the idea is that if, let's say, you set a wrong config key, or a port's not open, or, you know, whatever, like, we want to report that to the user as quickly as possible, and not leave them in a state where they think things are working.
But in fact, they're broken.
So, in general, anything that deviates from that, we want to be opt-in.
**Trent Vigar** 26:57 And… do you suppose that it's… that it's possible to update config on the collector that…
the op-amp server knows is… is not going to…
change the components at all, and I'll… what I mean by that is, like, let's say you've got an OTTL statement in a
a translation processor or something like that, and you're just updating a value, you know, like, you're updating a number 3 to 5 or something, and you're pushing that from the server, like, that's not going to cause the collector to, you know, have issues starting up, and if there's such a config change that
You know, you know is not going to cause any kind of problems with a restart, because it didn't change any of the components.
Is that something that we could treat differently, perhaps?
**Evan Bradley** 27:47 We've talked about that. That's a separate topic with its own set of thorns. That's, I guess we've called it hot reloading? Like, it's essentially, like, being able to do diffs, and then going through the component graph, figuring out where those changes are, and only restarting those bits.
That is also something we've considered, but, is, I mean, for better or worse, it's an entirely separate issue. Like, that would require, some…
Serious thinking through of how to make that work without losing any data, while restarting just those bits.
**Trent Vigar** 28:20 Okay, that's… that's really the use case that I'm looking for with
you know, trying to do these… this collector config updates, so that's really more what I'm interested in, so I'd love to look more into that and talk more about that another time.
**Evan Bradley** 28:33 If you pay me through Slack, I can send you an issue, or I think we've discussed… I'd have to look through the issue backlog, I can't remember, but we've had some discussions on that. The immediate recommendation I could make is if you…
And if you would be okay with this, you would… it would require some custom work and wouldn't be upstreamable in the short term, but you could, implement a custom version of whatever component you want to be hot reloadable like that, and then use an op-amp custom capability to perform those hot updates.
Again, this would be, like, a highly custom solution, it wouldn't be generally applicable.
But could get you to, you know, wherever, whatever state you want to be in in the short term.
**Trent Vigar** 29:21 That's helpful. Okay, thank you.
**Mikołaj Świątek** 29:25 Yeah, the hot reloading of the whole component graph is a… is a big, big hole.
it's probably easier to get there with small steps. Even, probably, even just leaving alone the pipelines that you know haven't changed would already be, like, a…
Significant change without even trying to do things like inserting receivers at the start or something.
**Trent Vigar** 29:56 Okay, well, I've got, a lot to look into here. I don't really know exactly what the resolution of my, you know, topic here was, but just to get some conversation going, and hopefully
we can keep the conversation going in Slack, and maybe some more at the next meeting, so I don't want to take up too much more time here, so I think…
Good to move on to the next topic.
**Pankaj Kumar** 30:25 I think mine is next.
Great.
Hi, everyone. So, a few days back, I suggested
the auto discovery support in the Windows Event Log Receiver.
So, it is the extension of the functionality of this receiver.
So, basically, in this, I want a functionality to auto-discover the… all the receivers that are installed.
on the particular domain, right? And the domains are also auto-discovered based on a flag that we will pass.
Into the config.
So, I have an issue raised for this already.
And once the issue was, like, accepted higher.
created a design for that, so I raised another issue with the design in it.
So basically, I want the input from the code owner.
I think Paulo is here.
Like, how we can proceed as well.
**Paulo Janotti** 31:26 Yeah, I'm gonna take a look, today and tomorrow's
And if I have any feedback, I'll put on the issue. But just a heads up that, after this Friday, I'm taking some time off, and I'll be back just, in January, but…
before my break, I put some… I will review in detail your proposal there. I think overall it's a good idea, so, I'll go back and forth with you over the issue in GitHub.
**Pankaj Kumar** 32:01 Okay, so, like, I just want, like, your feedback, and if you are okay, I can do the implementation in background.
Once you're back, you can review that PR.
But I just want the, like, inputs, like, if it is okay or not.
**Paulo Janotti** 32:17 Yeah, I, I, I oughta say that,
Unless you… if you already have the code based on the proposal, go ahead and feel free to open the PR.
If you are still gonna code, then I'll say, oh, okay, give me, about 1 or 2 days to take a look at the proposal, but depends on you. If you already have the code, feel free to open the PR.
**Pankaj Kumar** 32:44 No, I don't have quota yet. I will do it once the feedback is done.
**Paulo Janotti** 32:50 Okay, okay, sounds good. Thank you.
**Pankaj Kumar** 32:53 Inc.
**Mikołaj Świątek** 32:59 Okay.
I'm next.
So… For those who don't know.
when you emit status from components into the collector core framework, there's a kind of funny little state machine in there. And that state machine checks whether the transition that you're trying to do
between different statuses, is valid. And if it deems it not valid, it just drops it.
This is largely fine, and I think… I looked at Matthew… Matthew Ware's original PR implementing this.
I think the reason it exists is just to potentially drop statuses that are not… that are unnecessary in there.
However, we've recently added attributes to status events, and the intent… so the intent… basically, we have some generalized metadata that you can get… that you can attach to a status event. The…
driving use case behind that was to be able to emit statuses for subcomponents. And the primary, kind of, untrue use case was,
the, receiver creator.
in Contra, because on the receiver creator, you can have a bunch of receivers running, and there's no way to actually report status for them right now, because you can only, like, report a single status for a couple.
So we added attributes, this is great.
But the problem now is, if I emit a status that is… if I emit a status event, where the status is okay, and my component's already in that status, it will just get dropped.
And it doesn't… and this is actually very useful to do, like, just emitting the same status with different metadata. Even if you're… the… under the current framework, doing sub-component reporting is basically impossible because of this, because…
The framework enforces when you… when a component emits a status event.
this is… this has forcefully has the DAT component's ID attached, so by definition, if you want to report statuses for subcomponents, you have to do it via some kind of convention.
Via metadata, but if your… if the status of your top-level component doesn't change, and it's still okay, or recoverable, or whatever.
Again, nothing passes through.
So, I basically would like to relax that requirement, and at least allow… The,
statuses with the same… events with the same status value to go through. So, if… if the status… the collector think… if the collector thinks a component is healthy, it has status OK, then… and it gets another event with status OK, it…
Pushes that forward to all the, to all the, listeners.
And similarly, I think this should be the case for recoverable error, for kind of similar reasons. I think it might even be useful in general, just because even if you're in an error status, that error status might become…
You might get more information.
about the error status, or you're in an error status, and the error… the reason for the error changes. That can also, like, very easily happen with, for example, network connectivity, right? You can have all sorts of funny reasons. You can reach a remote, and it can… that's a situation that can evolve.
over time.
So basically, I wanted to see if there's any
any immediate reasons why this cannot be done, because I'm unaware of a reason this is done this way. Right now, the only upstream consumer of these status events, I believe, is the HealthCheckv2 extension, that I know of, anyway, and that extension aggregates the statuses anyway, so it doesn't care.
that we emit something twice, for example. It doesn't make any difference.
**Evan Bradley** 37:10 I, I wasn't involved too, too closely with the,
the initial implementation of component status. I did follow it a little bit, but, didn't deeply review the PRs, but I don't see any reason, off the top of my head why,
We wouldn't be able to do this for the points that you made.
I mean, if you think about it as a, you know, like a graph, like, I don't see why the nodes can't have a loop, like, what… what harm is… does that cause?
**Mikołaj Świątek** 37:37 I think the reason was just to avoid just spurious status updates.
But I don't think that's, like, a practical concern right now.
And we can always, like, either immediately, or we can go back later and do some kind of, like, content-based hash on it, if we want to avoid reporting the same thing twice. It is, like, it's not a big deal. And this is gonna be a very, very simple change that won't really…
affect much. The Health Trackv2 extension is still in alpha.
But anyway, if anyone has a… if anyone, you know, if anyone has… has… has a reason, knows of a reason why this might be problematic, please let me know under the issue.
**Andrzej Stencel** 38:21 Yeah, I don't have a reason, I agree. I like your points, I like the examples that you gave very much, and I think, if I recall correctly, this was done… preventing state to the same state transition was done purely for performance issues, to prevent…
Spurious events, as you said.
And, yeah, sure, like, world has changed, we've moved on, time has shown that this is not an issue at the moment, and then… but the attributes, it seems obvious that we need to allow that, whether we want to introduce the hash or not.
maybe we don't, as you said. If there's… if we don't see this danger, happening, maybe we don't need a hash, and we can always introduce it later, right? Makes sense to me.
**Mikołaj Świątek** 39:07 Alright, cool. Thank you. So, that's… oh, I… yeah, sorry.
**AK Andy Keller** 39:11 Sorry, I just put it in chat, but as… and I'm sorry, I'm very late to this conversation, but when we implemented Component Health in OpAMP, we made the structure recursive.
Is there any appetite to doing that? It would be nice if these matched, but… .
**Mikołaj Świątek** 39:29 Kind of, like, so that's kind of what we're doing. We didn't want to be overly prescriptive, so this is what… I can link to the issue if you want later, where this was discussed originally, how to do it, because originally this was the problem that we were trying to solve by… we ended up adding attributes to the status event.
And the reason we ended up… and one of the approaches we considered was literally doing… literally doing this, as in recognizing that, yes, you know, an event can have sub-events, and in fact, if you look at the implementation of Health TrickV2, this is how it looks like in there as well.
And in the end, we decided that we wanted to… we didn't want to commit to this. We wanted to do something more generic and kind of, flexible.
So, we decided that we're going to add attributes. It does literally, like, a P common map. You can put anything that can go into PData in there. And the longer-term… the longer-term intent is to change the status events into literally PData events.
And so, there's going to be… I don't know if there is already a conversation about this or not, Christos Markle would know it, and I'm not sure if he's here, but the intent is also to have just, like, a semantic convention for an attribute that tells you this is a subcomponent of something.
And then you can kind of rebuild the graph from this information, if that's what you want to do.
**AK Andy Keller** 41:08 Okay, that makes sense. I think, minimally, we should probably update op-amp, to support attributes.
To try to keep them… In sync, as much as possible.
So, thanks.
**Mikołaj Świątek** 41:26 Okay, Andrew?
**Andrew Cholakian** 41:28 Yes. Next.
Hello, everybody. I wanted to spring a little…
attention to this PR and see if there's some feedback on adding context inference to the routing connector. So, as a quick recap.
you know, today, the routing connector, you wind up using this syntax, and with inference, this is the PR, you would be able to instead use context inference and just get rid of that context block. So what this PR does is just adds it
Adds this ability to the writing factor as is, doesn't really change much else.
Now, one of the questions I had is, it sounds like EDMO reached out to some code owners, actually, just before this meeting, and after I'd put it on the agenda, and heard some positive feedback for this kind of approach, but I thought I'd open it up for discussion.
I'm here, and I have something else on the routing connector right after this, too.
**Evan Bradley** 42:28 So, yes, thank you, Andrew, for bringing this up. I… Admo did talk to us about this. I don't remember exactly what the last messages were, but, in general, we're supportive of trying to add,
like, the context and the paths here, and infer it and all that, I think what we're trying to decide right now is exactly what the config syntax for that will look like.
**Andrew Cholakian** 42:52 look like.
**Evan Bradley** 42:53 So for example…
in the README here, there are some, what do you call it? There are cases where, let's say, you're dealing with multi-tenancy. You have a key come in on the resource that says, like, you know, this data belongs to this tenant.
and you want to send it to a particular backend, endpoint based on… or using the routing connector based on that, you might want to remove the tenant ID from the resource, because you don't need it after that.
where it belongs, right? So for those cases, you'll have, you know, a full statement,
And I guess, really, the only thing I'm saying here is, you know, how do we format it so that most people don't need this, but at the same time, you know, you want to be able to sometimes do these sorts of things, with…
Okay, let me… let me back up. So…
You… you have a statement, right, that has the editor and the condition, but most times you just need the condition, so how do we make it so that you can easily configure this so that it works for most users with the minimal amount of config?
but doesn't, limit us to not, be able to do things like that. So I don't know what the resulting,
config schema will look like, but overall, I think that we are, we're in alignment that we would like to see something like this going forward.
**Andrew Cholakian** 44:18 Cool. Well, I had another option I was actually thinking of that's not in the PR for this config syntax as well. I don't know how that fits in with what you were just discussing.
I had started tackling another issue for dynamic routing, where you could, you know, have the… I'll just show you what that would look like, where you would be able to dynamically compute the name of the pipeline. Now, I actually came to the conclusion after working through a PSC that was functional that
kind of don't think it's worth the complexity to add this feature. Like, there's certainly some uses for it, but, like, it comes at a cost, of course, of code and maintenance. But I was thinking, you know, it is nice to have this kind of one-line syntax also, or maybe you just have this static syntax.
As an alternative, where you can just kind of collapse the whole multi-option thing into one, into just a list of strings for the table. So that's another option to think about.
**Evan Bradley** 45:11 So, I will say that from OTTL's perspective, the dynamic syntax is no more complex than the static syntax there.
**Andrew Cholakian** 45:18 I mean, sorry, from the OTTL perspective, yeah, but then you have to worry about dynamically routing stuff to.
**Evan Bradley** 45:23 Oh, yeah, that's true. Yeah, that will… it'll get funky.
**Andrew Cholakian** 45:26 Yeah.
**Evan Bradley** 45:28 So…
Yes, I… we were… we were looking at… I… yeah, I don't… I don't have any… I don't have any concrete feedback right now. I'd really need to sit down and think about it, because Edmo did pass this to us, and with the delete key, editors, the question is, how do you use this syntax with those, given that those don't…
Except an output, pipeline as an argument right now.
**Andrew Cholakian** 45:53 I see, I see. And just… is there, is there an example of a delete key syntax? I wasn't… I didn't actually… I saw something in the code about it, but I didn't actually look at what the syntax looks like.
**Evan Bradley** 46:03 The docs are not good.
**Andrew Cholakian** 46:05 Okay.
**Evan Bradley** 46:05 I could send you something. I sent them something.
**Andrew Cholakian** 46:08 Okay.
**Evan Bradley** 46:08 I had to do, like, a proper grep through the code to find it. It is there, it does exist, but it is, unfortunately poorly documented.
**Andrew Cholakian** 46:19 Okay.
Well, I'm glad to be in touch over it, and I've updated the relevant issues. I'm going to add a comment around the dynamic stuff to the one I have, but I think, even so, it makes sense to add the inferences, because it doesn't… it's just a progressive enhancement. It doesn't take away from existing syntax, as far as I know.
**Evan Bradley** 46:35 Right. I think that in general, we would like to see the transform processor, filter processor, and routing connector have as close of a feel as possible.
Obviously, you know, they all serve different purposes, and we want to make them, you know, work for their purpose, but, you know, ideally, a user goes between any of the three, and they don't feel like they need to, you know, relearn everything from scratch.
**Andrew Cholakian** 46:57 For sure.
For sure. Yeah, and that's why I think I like the single, simple syntax that more aligns with that. But you can have both, and I can see the use case for still keep using the other one, which is, like, maybe you're using Ansible to provision your config, and you'd prefer to templatize things in
Or maybe not Ansible, but you'd prefer to have a structured YAML field for the pipeline, as opposed to having it be part of a string. I think it's still nice that we have the older syntax.
**Evan Bradley** 47:21 Right, yeah, we'll have to discuss that going forward. I would ideally, at some point, like to see us expose OTL's AST so that you can have users type these things in, but then you can provide some ways to template it in more of, like, a structured format, without necessarily needing to provide both through the YAML config, but,
Yeah, let's, I don't know, we'll discuss that in issue going forward and see what makes sense.
**Andrew Cholakian** 47:45 Sounds good.
**Evan Bradley** 47:45 Yeah, sorry, I don't have a whole lot of answers right now, but thank you again for driving.
**Andrew Cholakian** 47:49 That's alright, just here to raise awareness. Thank you.
**Evan Bradley** 48:03 That is all we have on the agenda right now. Does anybody else have any topics that they would like to bring?
If not, then I think, we're gonna call it.
Okay. Happy holidays, everyone.
