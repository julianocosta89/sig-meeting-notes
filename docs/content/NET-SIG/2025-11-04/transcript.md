SIG: .NET SIG
Date: 2025-11-04
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello** 03:04 I'm gonna guess no one else is gonna turn up at this point.
Is there anything in particular either and you want to discuss today?
He's right.
**Matthew Hensley** 03:37 I did have one topic about, the instrumentation suppression stuff being baked into the SDK package.
It's come up again in Contrib, and might be time to solve that.
**Martin Costello** 04:02 Sorry, I just realized I had the wrong audio source turned on.
I didn't hear anything anyone said when I was talking.
**Matthew Hensley** 04:18 Oh, you didn't miss too much.
So I'm gonna put a thing on the agenda.
**Donald Hanson (OpenTable)** 04:30 Hello, can you hear me right?
**Martin Costello** 04:33 Yes.
**Donald Hanson (OpenTable)** 04:34 Awesome. My name is Donald Hansen, and I work with OpenTable.
And I had a topic, so should I tack that onto your, Google Doc.
**Martin Costello** 04:44 Yep, sure.
Did you have anything for the agenda today, Rajwahana?
**Hannah** 05:33 No, I'm just here to listen.
**Martin Costello** 05:36 Okay.
Welcome.
This is the most people we've had for a while.
**Alan West** 05:54 Hey, everyone.
**Rajkumar Rangaraj** 05:58 No, I'll… let me see if I… I'll help drive today, I don't think anyone has started it, right? Yeah.
Given I had this topic for discussion, the first one, which… Got added by… Matthew here, I believe, like, the reason, behind that is, like, Pietro engaged us in the background to… discuss aboard this one.
So, even before I speak about it, like, Matthew, can you go ahead and explain what's the exact ask, so that we can… Discuss further about it.
**Matthew Hensley** 06:52 Yeah. Fairly straightforward. We have, you know, the SDK can be told to skip instrumentation.
For certain clients, it makes sense.
You know, like, the ElastiSearch client's a great example where it uses HTTP under the hood, but doesn't necessarily want to expose those spans.
But as of today, you have to take a dependency on the SDK package.
To get access to this suppression instrumentation stuff.
It's not part of the API, necessarily, and ends up with a weird dependency.
That… Probably shouldn't be there, but it's also the best option.
So I've linked to the comment about… that brought this up again. Obviously, you're aware of that one, Raj, but also dropped a search there to some of the places that use this and contribute. There's a few instrumentation libraries.
that are using… this and have taken the dependency, and there's other ones where we'd like to use it, like the HTTP client or ASP.NET instrumentation, that we don't want to take the dependency, but do want this functionality, so… probably need to make a decision about where it should live.
And… So it's actually usable for everybody.
**Martin Costello** 08:08 I had a quick look at this the other day as well, and the property on that type just redirects to a property on another type.
Which I think is in the API package.
Sorry, no it's not. But then that's just wrapping some internal stuff.
So… Potentially, I thought one thing we could do… is… have… Sorry, that's another type in the, the SDK, but then that depends on stuff in the API package, so you could maybe just push it all down.
make… The existing stuff depend on that moved part.
And then just mark stuff as obsolete, because otherwise, I think you'd have to do a braking change.
**Rajkumar Rangaraj** 08:57 So, even before we jump onto the solution, I just want to understand the, idea behind the… why this feature first made it in the SDK, not in the API layer. If I recall correctly, Alan and Raylee worked on this earlier, I believe. So, Alan may have more context here. I think he has also joined, so he could shed some light on… for us here.
**Alan West** 09:23 Yeah, it's been a long… been a long time since we've talked about suppressed instrumentation. I mean, this was… as you said, something that Riley was working on, I was a part of that as well.
it… It's not a thing from the spec, so that's one thing that makes this kind of an awkward feature.
that has actually landed in our… in our stable SDK.
And because it's not a part of the spec, is exactly why it's not actually a… a public-facing-like thing in the API, which is where it probably should be, right, in terms of the specification.
There are open issues. I was actually just trying to search for them, and I'll continue to search for them in a minute, but… Like, long-running, like, issues that have been open for years and years and years, because this is a… This is a common need, for effectively suppressing instrumentation.
The… so, right, that'd be one avenue, is to… try to breathe some new life into, moving, moving the spec on this.
that would probably be hard. I mean, just… I think people are interested in it, but it's just… it hasn't taken a, like, a front seat, like, priority-wise, so I think it would be hard to, get… people moving, but I think that that is technically, you know, the right way of going about this need.
To the point of Peter's, like, comment on this, just some historical context, we… Had previously used the… Suppress instrumentation in… I wanna say, I think… I think the gRPC… that's what it was. It was, like… it was like the ASP.NET Core instrumentation also supports gRPC, and it was using suppressed instrumentation, I think, to suppress, similarly, like, HTTP client calls.
My mind is a little bit fuzzy on the… on the history there, but in any case, prior to making that instrumentation stable, we… Tore all that out.
Basically, because we did not want to take a dependency on the SDK.
So… Anyways, that's what Pyotr's basically saying in the context of this instrumentation, but it doesn't leave us with any great options, right, unless we were to do… That spec work.
Basically.
Because, Martin, as you point out, we want to avoid a breaking change, we don't want to, like, move… it's not just a simple matter of just moving the API from the SDK, you know, that's there, it's stable. And we also don't want to introduce new APIs to the API, that are not SPEC compliant. So… It's, funky situation, needless to say.
**Rajkumar Rangaraj** 12:55 Thanks, Alan. I think it makes more sense now.
Any questions anyone has on this topic?
**Martin Costello** 13:06 Yeah, I think my only comment on maybe it could be not moved, but, delegate to a new… API of sorts is because it seems like the meat of how it worked is actually defined elsewhere, it uses runtime context, which I think is in API, but I might have dug through, the code in the, put my pen material correctly.
**Alan West** 13:37 No, you're right about that. The… the… the… the… that's correct. The… the runtime context stuff lives within the API package.
And that's…
**Martin Costello** 13:51 Yeah, cause…
**Alan West** 13:51 Suppressed instrumentation is leveraging, essentially.
**Martin Costello** 13:55 Yeah, because looking at it, it's just eye disposable wrapping and setting a Boolean around that, so, like, the… in theory, the redis instrumentation issue could be solved by… Reimplementing that inside it.
Because ultimately, it's setting the same central point, but it would be very brittle and hacky way of doing it.
Assuming that nothing else needs to look at the same property to know if it's on or off.
Unless it would… because they're looking at the same backing field, that would work anyway.
a higher level. Like, the static property would still be… correctly set.
**Alan West** 14:47 Right, and it's… There'd need to be some coordination, right, between… it's not all contained to the Redis instrumentation, right? There needs to be some coordination with, like, the HTTP client instrumentation, right, which would Basically say, like, Don't do anything if this… If I'm suppressed.
Isn't that right?
**Martin Costello** 15:18 Oh, no, what I was thinking more is, because the ultimate is, am I on or off?
Seems to be… sort of hidden away.
you could move it a layer down and just have all the existing APIs call to the new one.
And then the Redis instrumentation could point at the… Like, the effect to, like, the underlayer that's the replacement. And then everything would still be looking at the same value.
But you… Then have, like, two ways of doing the same thing, and then you'd want to eventually deprecate The older one.
**Rajkumar Rangaraj** 16:01 Martin, if I understand Alan correctly, his thoughts are, like, like, always, like, if you need to introduce a public API in the OpenTelemetry API layer, it needs to be strongly backed up by the specification. And this is a topic of discussion already there.
We further should invest in there, because if we do something now, and later from the spec, if the shape of that changes and comes in a different way, it will be in another thing. So creating many duplicates in the API layer is not a right thing. So that's why we always maintain a high bar here. Any public API that's been introduced in the repo is highly scrutinized and reviewed to see if it meets the bar with… along with the spec.
So, here, if I understand Alan correctly, the spec is the blocker, and we may need to go ahead and invest our energy there. And, based on that, we need to change the… the solution. Resolution may be very simple. Even I remember that part of the code. I remember reviewing that.
when Alan and Rayleigh did that work. The… It's not about the resolution, it's about how we are going to get it done and align with the broader open telemetry goals.
Is that correct? Did I summarize correct, Alan, here?
**Alan West** 17:30 Yeah, that's… that's right. I'm still trying to wrap my head around what… what Martin's… the… the solution Martin is toying around with.
Still not quite following.
**Martin Costello** 17:39 Essentially, I'm suggesting that… some… a new type was added to API, let's just park whether that's a good idea or not to start with. Okay. Which effectively is the same implementation we already have, and then the existing classes just delegate to that new one.
And then the Redis one would just use the new one.
Because that's at the right layer, it doesn't need the new dependency. And then over time, anyone… anything currently using sdk.suppressed telemetry Would swap to the new property.
**Alan West** 18:15 Yeah, okay. And then in a future breaking, major change, you could delete the two from the SDK.
Okay, that's… okay, the part that I had missed before was where you were basically putting this implementation, in the API package. So basically, what Raj summarized is the concern There. I thought maybe you were trying to push… push some implementation of, like, suppressed instrumentation down into, like, the Redis instrumentation or something, and…
**Martin Costello** 18:45 Oh, no, no, no, but I did a tangent suggest that given that the implementation in the SDK package is ultimately just Reading through into the runtime context.
you could hack around it in the Redis repo by… because you know what it's doing under the hood, you can effectively have them mutate the same backing field. So it would be working without going through the public API, but only because it knows the internal implementation detail.
**Alan West** 19:16 Yeah, and so in that vein, I agree. That kind of thing sounds kind of hacky, but just kind of exploring that thought a little bit further, anyways, I… I… So, backing up just a second, so remind me again. So, basically, you're trying… Underneath the covers.
Redis instrumentation basically is making HTTP client calls, and you don't want to see those. It's using HTTP client somehow.
**Martin Costello** 19:46 I think it's more that there's a specific user has a specific use case where they don't want to instrument what Redis is doing.
I don't think it's anything to do with HTTP client.
**Alan West** 19:56 Oh, okay. They just.
**Martin Costello** 19:58 suppress Redis itself, and they can't But… so to do that, they added in… they changed the Redis provider to put the using scope in.
like, if suppressed, if not suppressed, don't… whatever it is. But then, to do that, they had to bring in a dependency on more packages into the Redis instrumentation, and then that's where the conversations come from, because It's bloating the dependency tree just to access the property.
Okay, okay, I'm… all the… all the stars are beginning to align in my mind now. I… I'm sorry, I'm catching up live here, I haven't looked at any of these issues, so…
**Alan West** 20:37 So, the user that we're talking about, this is, like… This is code that's not owned by the contrib project, this is, like, some user's code out there?
**Martin Costello** 20:49 And now I've got to double check.
The PR is called Support SDK Instrumentation.
And… right. So, inside the Redis instrumentation itself.
They've just made a change to not instrument if the property is true.
**Alan West** 21:15 Right, okay, and this is some user, and they are, of course, taking a dependency on the SDK.
And they want to be able to use the suppressed instrumentation API, and they just want the Redis instrumentation to honor it.
**Martin Costello** 21:28 Yes.
**Alan West** 21:31 Got it. Okay, I thought this was a… I thought this was the… Example where we were basically, like, you know, trying to… Control… things between instrumentation that we own here in this repo as maintainers, but… Not so much.
Yeah.
We don't have a good answer for them, I don't think, at this point. I think we'd… I mean, I guess to your point.
You could… you could shove… We could do the hacky thing, as you suggested.
**Martin Costello** 22:19 I'm not suggesting it's a good idea.
**Alan West** 22:21 No, no, I agree, but it's always good to talk out bad ideas sometimes.
Because sometimes… sometimes it's a… Sometimes bad ideas help, Where my mind's going is, like, if we can implement a bad idea, you know, sometimes it helps, like, prove another, like, use case and provides kind of, like, a prototype of sorts to help move, like, specification conversations forward.
So, sometimes, sometimes doing kind of achy things.
Helps in that way.
But I don't know if this necessarily… Qualifies as a situation where we should do that.
But the nice thing about the achy idea is that, yeah, we could probably do it in such a way that it wouldn't expose us to an SDK dependency, and also, of course, doesn't change, like, you know, public-facing API of the Redis package in any way.
And if we… If we came up with, like.
an icky implementation that could, you know, somewhat be centralized, and maybe shared among… I mean, if… you're right, if we open it up to the Redis instrumentation, it opens up this, like, slippery slope to, well, we did it in the Redis instrumentation, why don't we just do it in all the instrumentation in the contrib repo, right?
So, that's… that's a component that makes the idea even, you know, additionally icky. But maybe in… maybe we could mitigate the achiness to a degree by thinking about how we'd implement that in kind of a central way that could be shared. Again, I'm not saying any of this is a good idea either, but… I wouldn't be opposed completely to entertaining it as a… As… as something to… Move conversations forward.
So I'd be okay if somebody were to, like, basically… just prove it out. And we could all just kind of, like, discuss it and… See if it's something we'd want to move forward with or not.
**Martin Costello** 24:55 Yeah, that sounds, reasonable to me.
**Alan West** 25:04 How do you feel about all that, Raj? I don't know.
**Rajkumar Rangaraj** 25:07 Yeah, that makes sense, yeah.
**Alan West** 25:18 I'll keep trying to look for those, spec issues. It's been a long time since I've looked for those, so I… I don't have them.
handy, but I can try to find them in case anybody wants to… read up on them, and maybe even see if there's any interest.
From the spec group.
Dusting this conversation off.
**Rajkumar Rangaraj** 25:52 Let's move on to the next topic.
**Donald Hanson (OpenTable)** 26:02 was mine.
So yeah, if you… This topic, I think, came up with this group, a few months ago, And, it's kind of hit us at the OpenTable side. It has to do with, how we can use the scope log attributes, and what we can do potentially to modify them. These examples are a little different from our scenario.
Where obviously they're beginning a scope with a string, and it's got, you know, its values and everything in it. What we end up doing is… We pass through a dictionary that's got a bunch of keys and values in it, in, you know, begin scopes across the board. Where we're trying to go is we're trying to migrate from, like, an in-house old platform that we built for logging, on the Elk stack over to OTEL.
And… In order to do that, we've made a pass through, specifically my team, to try and standardize on as much of the hotel conventions as we can on the names and the fields. So we have a lot of legacy things that we had, That we would like to go through and rename, for example, or potentially drop.
Whether that's, like, information about the host that you're on that's now in resources, in the resource attributes, or if it's, renaming it, for example, if we know something about, like, in this case, stuff is running in Kate's.
So we kind of want to get a shot at modifying, some of the information before it gets exported. So it's somewhat related to this, of being able to control, the log attributes and the scope log attributes. I think there was a, A suggestion, a few months ago about putting a, an option, or a wrapper around it, or something like that. I wasn't clear on the feasibility of it.
**Alan West** 27:50 In kind of that scenario.
**Donald Hanson (OpenTable)** 27:53 This example, this team was concerned about the fact that they, internally in the exporter, the attributes, they're… they're trying to dedupe them in their scenario.
And so they were coming up with an alternative on that process and a suggestion on it. I wasn't so much married to the recommendation in this PR, just more of the context around the use case.
So, can I elaborate, or any questions initially on that?
**Rajkumar Rangaraj** 28:22 It's better if you elaborate slightly, a bit more on what you expect from it.
**Donald Hanson (OpenTable)** 28:29 Yeah, I can actually show you exactly what we're trying to do in our processor, and you'll kind of get a snapshot.
If you don't mind me doing a quick screen share.
**Rajkumar Rangaraj** 28:37 And stop the sharing.
**Donald Hanson (OpenTable)** 28:42 Yeah, let me see if I can just do the one… Okay.
Right, so… This is our, log processor that we're trying to pipe in on the hotel side.
And I have… it's somewhat of a fictitious example, because we recognize, that we would not be doing this, we would use a lot of this with tracing. However.
we didn't have tracing prior to this, so currently at our org, we use logs to collate a lot of this information. So in this example, we're using logging with a bag of fields, and you can see some of these examples down here, and say, hey, we want to map a lot of these things across.
We want this log message to show up in both our old Elk stack and in our OTel stack, but anything sent to OTEL, we want to rename several of these fields.
We want to drop some, we want to move them around, but we obviously don't want to change, you know, our team's applications to do that if we can.
So what we've… our thought was initially, can I use a processor to go rewrite them? And of course, I can do that with log attributes. Those look great. And so effectively, we do that process here. We walk through the whole list, and we do this whole mapping that we're going to replace them. And so here's a laundry list of… Things that we might choose to do.
Are we gonna change the service name? Are we going to drop a UID field we had? Are we going to prefix some of them? Are we going to drop them completely? This is kind of some standards, and we have multiple stacks, so we've got a Java and a JavaScript. On the Java side, they have a better control of some of this stuff.
they're not using scopes. So I don't want to get too hung up on the different language stacks, but… That's kind of the general idea, is I got to this point and I went, I can't modify that scope key.
So what do I do?
So…
**Martin Costello** 30:32 This… it's not inside OTEL, but this rings a bell with stuff I did at my previous job.
And we did a similar thing, but we did it inside the iLogger infrastructure.
But I don't have access to the code anymore, so I can't, look at it to refresh my memory.
But I remember doing a similar thing there, where we effectively had a similar thing with the Elk stack, where we wanted consistency of naming, so using a shared internal library that everyone used, we just did the renaming in there.
But we weren't fully adopting, OTEL at that point, so that's why we did it within iLogger. So… whilst it's… tangential to the issue of how would you do this in OTEL, for your specific use case, you might be able to do what you're trying to do in the iLocker infrastructure.
**Donald Hanson (OpenTable)** 31:38 Right, and what… how would that play within the… blogging provider. Basically, it's a wrapper of some kind, or… Just to walk us, and I know you don't have it. If I remember correctly.
**Martin Costello** 31:53 it was, like, a scope processor, or something like that, within… within the iLogger, not scopes to do with hotel.
**Donald Hanson (OpenTable)** 32:02 Yeah.
**Martin Costello** 32:02 And we process things as they would go, like, you know, before they get to the point where something gets actually logged.
And then if iLogger is plumbed into OTAL, then by the time OTAL gets it, you've already changed it, and then it will just go off as if you've done nothing.
**Donald Hanson (OpenTable)** 32:21 Would that affect both providers, because effectively we have two logging providers. We have one that publishes things to Elk, and a completely separate one, obviously, which we'll publish it out to.
hotel.
**Martin Costello** 32:34 Without the code, I can't remember.
**Donald Hanson (OpenTable)** 32:36 That's right. You can make it… Yeah, I think I… I think I looked at that. It's like a scope provider.
like, I was trying to figure out how to inject that, or how to wrap it specifically, And how that gets captured, because effectively, the begin scope delegates the data over to a scope provider, and the scope provider maintains it.
M.
And then obviously cleans it up and stuff, so… Okay, so that's an area I can look at.
For sure.
More in-depth, so… Yeah, the general thought process was, right, how… could I or should I be able to do this? I think, should I is a very valid question.
So… At least from your, kind of, the hotel perspective, so… I think there was an alternative proposal, which somebody submitted a PR for, and I can't remember what it is exactly, but it effectively separated include scopes.
And exclude scopes.
In, the field, because currently those two are commingled.
So, an alternative would be if I were to, in this processor, I were to walk these keys, and I were to push down the scope attributes.
down to the log record, I would get the goal I'm looking for, although semantically, technically wrong.
But then I would not want the scopes exported.
Does that alternative make sense?
**Martin Costello** 34:15 I think it makes sense to me, in terms of what you want.
But I don't have in my head how it would translate into the logging infrastructure for hotel.
**Donald Hanson (OpenTable)** 34:26 The, I don't know a… might be able to find… Oh, it was a PR, actually. Let me see if I can find the PR real quick that, Somebody had submitted, Now, we'll see real quick if I can search for that, but it was, like… It's actually mentioned… yeah, it's a PR. I have the PR, it's right here in the ticket.
an issue. Right, so the alternative one was… Let's see… This was part of their initial request back in June as well, which effectively was kind of what they're trying to do.
It's a little hard to read, but the end result is actually pretty straightforward once you look at the change.
They were asking for a field that basically says, I don't want to… I don't want to export scopes, effectively. This is the Protobuff logger saying I don't want scopes output.
The problem with it is that there's a field called Include Scopes, which captures those scopes, And then… No way to not export them.
So I could write a processor that says, hey, I want to include the scopes to capture them, but I don't want the exporter to actually put them out.
In which case I could put a processor in that would move them from… The captured side, and push them into log attributes.
And that's what this guy's intent was, initially.
So… So either of them would functionally solve my problem, I just don't know if that's something from your perspective, your group, if that makes sense for you guys to support in some way.
**Alan West** 36:31 I think the dream would be for… You to be able to… manipulate… Scope attributes within a log processor.
But we have… There's some things that make that complicated.
For us, and we haven't quite settled on a… A way to make that happen.
But I think that that would be the ideal end state, is that you'd be able to do basically what you're doing inside of a log processor.
**Donald Hanson (OpenTable)** 37:10 Gotcha.
**Alan West** 37:11 We just don't support it today.
But I think… I think it would be nice if we did.
Martin's probably right, you could probably skirt around our limitations by maybe, you know, exploring something just within iLogger itself.
But yeah.
I don't have a good answer.
**Donald Hanson (OpenTable)** 37:33 For this.
Do you guys have a direction? Like, I may have capacity to potentially contribute, but if you guys don't have a direction, I don't want to… go in the wrong direction for you guys. So, no is okay, obviously.
**Alan West** 37:46 Yeah, we don't really have a direction. I… the… the issue that you were pointing to, I've actually spoken with, that engineer, I had a call some number of months ago, Jeremy and I spoke with Jeremy and Steve, both from Elastic, who wanted to make some progress on that issue.
And I spent a little time kind of catching them up with the history of You know, why it's such a sticky issue for us.
**Donald Hanson (OpenTable)** 38:15 Yeah.
**Alan West** 38:16 Largely, the… my memory is a little bit fuzzy right now, so I'm trying to page all the details back into my mind, but the… One of the things that makes some of their… some of the ideas that they're… they've pitched on that issue problematic is that it depends on making changes to the OpenTelemetry, or the OTLP exporter.
**Donald Hanson (OpenTable)** 38:42 Yep.
**Alan West** 38:43 And ideally, This is functionality that doesn't belong within the OTLP exporter, it belongs more in the, log SDK.
itself, because… Manipulating… the desire to manipulate scope attributes should apply to, all logs exported, irrespective of how they're exported, whether.
**Donald Hanson (OpenTable)** 39:12 Yeah, I gotcha.
**Alan West** 39:13 OTLP or, you know, some other exporter. Like, we have some exporters in the .NET contrib repository, for example, that wouldn't benefit, right, from any changes that we made only to the OTLP exporter.
**Donald Hanson (OpenTable)** 39:29 Yeah, yeah, which is why you basically want to modify the log record before it gets to your exporters.
**Alan West** 39:34 Right, and so… that… That's where it gets tricky for us. The… I guess… You know, the work that… Needs to be done is somebody needs to kind of, like.
find that direction for us. We've just not… we've… we've not had the bandwidth As a group to do that, But by all means, like, if that's something that you have bandwidth for to… to… to play around with, and maybe propose a direction, that's… that's basically the conversation that I had with Jeremy and Steve some number of months back.
**Donald Hanson (OpenTable)** 40:13 That's totally fair. Yeah, I mean, it's all good. I will work internally and see what I can do to get some time on that, and if I can, I will come back to you guys with a potential proposal.
**Alan West** 40:24 Sounds good.
**Donald Hanson (OpenTable)** 40:25 Yeah, that's awesome. So, that's all I had on this one, so… Thank you.
**Rajkumar Rangaraj** 40:45 So, just taking it back further.
Let me take a look at the… be our artist.
Chatting my screen, let me know if you're able to view it.
**Martin Costello** 41:22 Yep.
**Rajkumar Rangaraj** 41:23 Cool.
So I think these can be reviewed offline, I believe.
This is pending, just wanna check, or… am I missing one more topic, like, I think today, without a name, it's been added. Even I had a question on this one.
**Martin Costello** 41:43 Sorry, that was me. Yeah.
**Rajkumar Rangaraj** 41:48 Yeah, let's discuss that before we move on, because I see that's one of the important topics for us to move forward.
**Martin Costello** 41:57 Yeah, so it was… it was just, do we still plan to merge this and have an RC, or is it waiting for GA now, because that's in a week.
**Rajkumar Rangaraj** 42:07 I would say we should do an RC, even at least we give few customers a chance to test it before we making it, and ensure that there are no breaking Changes in it.
**Martin Costello** 42:21 Okay, yeah, it's the only… so it's ready to… I'm not saying we merge it right now, but I'm just saying, technically, it's ready to go right now, there's just… you've got a block on it at the moment, Raj.
**Rajkumar Rangaraj** 42:34 unblock it, like, I don't recall. If it's waiting on me, I just.
**Martin Costello** 42:39 So, it just says, it's got a requested change from you on it still.
**Rajkumar Rangaraj** 42:45 Okay, it should not have that, because I remember, releasing that immediately the same evening.
So, if you look at it, I released it at the same day.
**Martin Costello** 42:55 I think it might be because… maybe it's a GitHub thing, because you haven't positively approved it, it considers it.
**Rajkumar Rangaraj** 43:03 Okay, I'll take a look at it. I already looked at it, looks good. That's what the thing I wrote. I'll go ahead and approve this one today.
**Martin Costello** 43:11 Okay, yeah, because, otherwise, I'll need to rebase it when 338 gets merged, because it's making changes to the routing tests that I'll need to react to.
If that one… the other one goes in first.
**Rajkumar Rangaraj** 43:25 Okay, this looks good to me. I've already taken a look at this PR when I went and blocked it before that, but this looks all good. I'll take a re-look. As many changes one more time, I'll take a look and approve this.
**Martin Costello** 43:39 Okay, cool. Because, yeah, I'm… as I can now, like, once it's merged, I'm happy to… Do the mechanics of, ship… publishing the RCs for it.
**Rajkumar Rangaraj** 43:53 Cool, yeah, thank you, Marty.
**Martin Costello** 43:59 But yeah, that was all I wanted to discuss on that one.
**Rajkumar Rangaraj** 44:04 just going back to the pull requests again, I already… I think these two can be done. Again, I think in… I don't know, this cosign, I saw at one point in time, Piotr had a… blocked this PR. I don't know whether he released and taken a look at it for us to merge.
**Martin Costello** 44:29 Yeah, I think, Renovate opened a PR for it, but there's breaking changes, so he fixed it up and tested it, and it looked okay to me, but the… the implementation details of how, as a consumer, you would validate it have changed, so there's, like, a new section in the README, and a few other bits and pieces.
**Rajkumar Rangaraj** 44:49 Okay.
This one, I had a look into it. I left a review note.
I think Hannah's also here, I believe.
I think it was… Some confusion around the… like… thing I left. So, if we go a few lines above, we will see this.
service provider being created. In case of the other implementation, we will see that the service provider is being disposed, but in this case, whenever we are just taking a no-op provider, it's not being disposed.
If you look at it, we have a logic in the other code saying that, do we own our service provider, or is the dependency injection going to own it? And the… or do the disposal of the service provider accordingly, as I highlighted here. That part is missing in… when we do the no-op, and there may be leak in the service provider. That's what we need to investigate on this PR.
**Hannah** 45:58 Okay, I'll take a look at it again.
**Rajkumar Rangaraj** 46:00 Yep.
**Hannah** 46:00 Yes.
Thank you.
**Rajkumar Rangaraj** 46:04 So, the other PRs are slightly moving at a slower phase. I have a slightly limited bandwidth. Martin, if you feel confident and some PRs can be immediately moved, just go ahead and ping me or Ellen it. We will help move it faster.
Or you or Piotr, if you guys feel it. Pyotr always brings such powers.
**Martin Costello** 46:29 Yep, sure.
**Rajkumar Rangaraj** 46:35 Cool, I think that's all I have with here.
Is there any other questions?
**Alan West** 46:46 I just want to note that, starting Friday this week, I'm gonna be out until the end of November.
So… I'll… I'll… I will be, at SIG meetings.
I do, though, intend on trying to… work on the database instrumentation, basically just get it over the finish line, it seems like. I think, there was a bug identified in the SQL processing stuff, that Steve has addressed, and… Anyways, I think that's all that's left there is to… is to… is to remove the feature flag and work on some documentation, and so I'll have a little bit of bandwidth, probably after this week, actually. But it's not a lot of work, so I'll just kind of do it while I'm out. And so, yeah.
**Martin Costello** 47:37 That reminds me, Alan, I had a quick look at the issue about the EF core stability for databases yesterday, and put some comments in there if you want to reply to that asynchronously at some point.
**Alan West** 47:51 Oh, okay. Sure, I can take a look at that.
**Rajkumar Rangaraj** 47:58 Cool, thanks for an update, Alan. I think… input.
Okay.
**Alan West** 48:09 Crap.
**Rajkumar Rangaraj** 48:09 then I think we could all drop off. Thanks for everyone. Bye.
**Alan West** 48:13 Yep, see ya.
**Martin Costello** 48:14 Bye.
**Hannah** 48:15 Bye.
