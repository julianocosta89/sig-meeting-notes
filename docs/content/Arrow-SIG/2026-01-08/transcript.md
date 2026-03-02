SIG: Arrow SIG
Date: 2026-01-08
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald** 03:06 Hi, everybody.
Let's see. This morning, I have learned that the F5 group will not be able to join us. They have an all-hands meeting, so every one of them is missing today. That makes us a smaller meeting than normal.
And I see…
four of my colleagues, so it's heavy Microsoft now, but we have some visitors, so I'd like to keep that in mind as we go forward and not have
Runaway Microsoft conversation.
So, good morning. I will share our notes, gonna suck.
While we're doing that, why don't you write your names? We can do this. Here's the…
I'm using a new mouse and keyboard, I keep telling people this. Having some troubles.
Here we are.
Alright, good morning, everybody.
Usually, we start meetings…
We've lost our standing agenda items, but, going to the issue list to see what's new.
All right.
While you're writing your names and your agenda items, I will open that.
Make my mouse behave.
Well, we're first week back from a vacation for many of us, so that's partly, going to explain a rather short update here for the issues. We have…
Most of this stuff goes back to before the holiday break, for at least for me.
And, and I don't know how far we need to go back exactly.
I, I'm actually, now that I know what we're looking at, I think we should start back at this, two weeks ago issue, Drew, that you filed, since I don't quite recognize it or know about it, and then we'll go and look through all the new stuff, since it's there.
I can keep my mouse under control. Is that…
**drewrelmas** 05:51 Yeah, I'm here, we can talk about that.
So this is actually a child issue of a parent. Josh, I know we talked in the SIG a few weeks back before the break about
condensing attributes being a supported operation on Attributes Processor. So we have syslog and Ceph.
And, a use case for… Seth that,
we have is this kind of catch-all operation to condense non-well-known Ceph extensions into a specific
single attribute. So, my example is here. If there are vendor-specific extensions in Ceph.
the desire to condense them to a single attribute for a back-end schema that expects something like that. We talked about putting this kind of behavior in the receiver, didn't really think
it was, widely applicable enough to belong there. Similarly.
We were hesitant about sticking this in Attributes Processor, so, there was actually my first PR merge about this that added a new experimental processor that is focused solely on Condense.
You can see, in the… in this issue down below, there should be a link to merged PR. Seems to be behaving the way we want. I was just tracking two additional issues.
One of them, if… once Attributes Processor supports, adding new attributes.
I want the condensed processor to make use of that, and then finally, I had a to-do from code review about instrumentation, which should be able to handle as we close on the internal telemetry guidelines, which I know is another.
**Joshua MacDonald** 07:58 Yeah, that'll be something we…
**drewrelmas** 08:00 I like his name.
Yeah, so I don't have any active, conversation on this. It was more of a to-do-for-me,
**Joshua MacDonald** 08:08 I see.
**drewrelmas** 08:09 In the future.
**Joshua MacDonald** 08:11 And I know that Tom, who's on the call, has begun working on what you just mentioned, the ability for the attributes processor to insert attributes. Is that…
Am I correct that these are related?
**drewrelmas** 08:24 Oh, that… that snooze to me.
**Joshua MacDonald** 08:27 Okay, I'm not… so maybe that was, a good coincidence. Tom, did you understand what Drew was, just referring to?
**Tom Tan** 08:36 Oh, I need to… get more details on it, it's not very clear, so I mean…
**drewrelmas** 08:41 I should… I can include a little bit more… I should include a little bit more of this issue, that's on me. Okay. I'll make a note to do that.
**Joshua MacDonald** 08:48 Okay.
**Tom Tan** 08:49 Okay.
Thanks.
**Joshua MacDonald** 09:02 Okay, Cool, that's what I just wrote.
So…
**drewrelmas** 09:09 Sounds good.
**Joshua MacDonald** 09:10 Right.
So, let's see,
Shared channel error handling, this is one that I asked Laurent to look into. I, I still have a little uneasiness over how we're handling, sort of, internal errors, like, when you are a component and you hand an error to the engine, what does it mean? That's sort of, like, a little bit… a little bit of an open question to me.
This seems, to be related. All errors are mapped to receive closed. Okay. I'm glad to see Laurent has picked up some of this, because he's the owner of the engine architecture, in my opinion, so we'll come back to him on error handling. We're not going to let that one go, I promise.
Okay, the, so, let's see… Flume MPMC should not be used with a sync interface,
This is…
almost the same. Nope, this is channel metrics. Okay, so the higher level that I can share with all of you on what I see happening here is that I have emphasized to Laurent that we
Are, like, sort of, like, code yellow on instrumentation, sort of self-diagnostic instrumentation of all kinds, and…
The idea that we are, we have a metrics infrastructure in place is good, but then, you know, if you look at some of the early components and some of the early code that we wrote, it's just like every component is instrumenting their own basic counters.
basic counters for pipeline stuff, and that's not a good way to go. And we knew this all along, but… so now the time has come. It's sort of become urgent, and I… and I see that Laurent is taking some responsibility, so this is a…
This MPMC is about… about channels and being able to automatically count stuff, which is what we're after.
I think we should not discuss it with Aleron.
So then, looks like Lowlet has a couple of updates here. I don't think he's in the call, so… but we can look through them. work has moved ahead on TLS, and I know that Lowlet's been, moving quickly on that. So this is a…
enterprise proxy level thing. Does anybody here know about this topic?
I…
don't, and I'm not going to try to invent an understanding right now. But what I heard was talk of, kind of, enterprise-grade features involving proxies.
Which I don't know about.
Same topic. I… this may be where I…
there was a… there was a PR discussion, and then now I want to find it.
I bet it was this… explain this, we can click in. There was a conversation between
Laurent and Lowett.
it's… it's about proxies, and I want to say that this is as much as I can absorb right now, but if you want to follow this topic, there are links and there's a PR where Lalit and Laurent discussed it.
Something about now coming to the hygiene issue. Maybe, Drew, you've got something to say here. I… I have…
**drewrelmas** 12:42 Nope.
**Joshua MacDonald** 12:42 I have struggled with our Weaver dependencies as well, though.
**drewrelmas** 12:46 Yes, so this was… we have Deny… Cargo Deny running on all of our CI jobs, which looks for advisories, as well as,
license problems with dependencies being built in our Rust crates. We had… there was a new advisory that popped up for
That is internal to our Weaver dependency, which locked all development from happening, because this is a required job.
So we… Temporarily have…
exclude… yeah, there's a PR link here, which shows the temporary fix.
the real… there's two things that really need to happen. First.
We need to… like, obviously, someone needs to make sure this dependency gets updated in Weaver. We would need to take the new Weaver version on our side. I know that there's a couple renovate…
PRs open for Weaver, but they're not easy in-place updates. I think there's some breaking changes, so someone probably needs to go do that manually.
The second thing I'd like to say is, should Cargo Deny block all CI work? You know, I know it protects us from a lot, but it also leads to these situations where
if it takes more than a day or two to resolve an advisory, particularly in, like, an… this is a twice-removed situation, right? Particularly in a downstream repo. Should that halt development work on our side?
**Joshua MacDonald** 14:29 Is there a way to make a distinction between dev dependencies here? I don't think of Weaver as a production dependency, so, I wonder if there's a way to loosen this… the impact of
Cargo deny on dev dependencies as opposed to pod dependencies.
**drewrelmas** 14:48 Potentially, I'm not sure, that requires some looking into.
**Joshua MacDonald** 14:52 Yeah, I don't want to go any further.
Okay, well, I think the other answer is for Weber to mature and get real with dependencies.
I don't know what Gick's date is, but I can't imagine why there needs to be another date library.
That was a… that was a little bit… bit of a invitation.
**drewrelmas** 15:13 Sorry, I laughed, but I was muted.
**Joshua MacDonald** 15:15 Okay, good. Somebody left, right? Okay, I don't know what gig state is, but apparently they've made, invalid UTF-8.
Yeah, at an earlier time in my life, I might have made fun of this, like, getting upset about UTF-8 validity.
And safety, and undefined behavior.
I've stopped. I'll let… I'll let it fly.
I don't quite understand the… anyway, that's not true. I understand it, I just don't believe it.
Okay, so I think this issue here is one that we are going to briefly summarize and not go into depth. I know there was a… there was a meeting yesterday for those of us who are studying the
But in Query Engine, and the use of Data Fusion, and abstract syntax trees, and our Microsoft's
KQL device.
I think that the high-level summary that I can give, and we can ask Drew if he has another opinion, the high-level summary is that it makes sense to split the two parsers. We're still aiming for an intermediate language that can be shared so that we have
when we have a data fusion filter over OpenTelemetry data, that it's just, like, that is an abstracted quantity that we can develop from both KQL or from a new language.
Is that fair, Drew?
**drewrelmas** 16:39 Yes, I… that matches what I took from yesterday's meeting.
**Joshua MacDonald** 16:43 And… I want to talk about this one now. Syslog CEF.
**drewrelmas** 16:47 Yeah.
So, I'm glad we have a Hukarsh in the room as well, because…
the primary, dev on that. I'm interested in his perspective, so…
I was doing some more in-depth testing of the Syslog stuff receiver we have compared to the Go Collector syslog parsing.
And I found a small discrepancy related to RFC 3164. The… I dug into the collector contrib syslog receiver, where they actually support producing app name and process ID attributes on 3164.
Even though it's not, like, a technical… to my reading of the RFC, it's not a technical part of the spec.
But it's some… it's, like, a very common pattern that is followed. The internal… so, like.
the collector conscript syslog receiver uses another internal parser for syslog, which I… that's the second code block there, where they assign, app name and process ID, because
it's, like, usually formatted in this way.
on our Rust syslog receiver, we only produce the tag attribute, and this issue is to talk about if we can change… if you scroll down, it has a better example of the current implementation. So.
In the syslog message, I'm talking about the part that says my app, bracket 1234.
All I'm trying to say is the Golang syslog receiver parses that as app name, myapp, proc ID 1234, but we only produce syslog.tag myapp1234. So, this was just a question of, can we…
attempt to, split that in a similar way to the Golang side.
**Utkarsh Umesan Pillai** 18:54 Yeah, thanks, too, for, finding this discrepancy, firstly, and…
I think this, should be possible.
Also, since the spec… the spec doesn't make it a hard requirement, but I think if it's a common enough usage scenario, then it's probably better to just do the…
Parsing of the tag itself to…
to segregate into app name and segregate it into app name and process ID.
**drewrelmas** 19:23 Yeah, I mean, it says there the format.
Is common, whatever that means.
**Utkarsh Umesan Pillai** 19:30 Yeah.
**Joshua MacDonald** 19:31 is usually an RFC term. This usually is.
**drewrelmas** 19:37 And also, I've seen situations, like, if there's no brackets,
I suppose… I'm not sure if it's…
correct to leave that as syslog.tag, and we could use Ashwood's processor to rename it into app name, or if we should still parse it out into app name.
I can.
**Utkarsh Umesan Pillai** 19:59 So, I mean, like, if there's no brackets, then do we…
Do we want to, like, duplicate the tags? Basically, the…
**drewrelmas** 20:08 Do you want to call it tags still, or can we… are we sure that we could call it app name, and just.
**Utkarsh Umesan Pillai** 20:12 I think Dad…
**drewrelmas** 20:13 tag it on.
**Utkarsh Umesan Pillai** 20:14 Tag was, like, was one of the fields that RFC31464 has, like, one of the, like, first-class fields, similar to hostname and content.
So I definitely think we should have tag, but
If it doesn't have a bracket, should we make it an app? Should we also populate app name with the same value? Yeah, that's a… that's a good question.
Yeah, but I… I feel like a tag… it's better to have tag always.
Because that.
**drewrelmas** 20:46 Sure.
**Utkarsh Umesan Pillai** 20:46 From what I…
**drewrelmas** 20:47 Could, we could.
Okay.
If the values are delta encoded, it's not too much worse if we have both tag and app name that have the same value. I'm a little hazy on that, but that's…
My initial thinking.
**Joshua MacDonald** 21:04 You're right, they would end up in a dictionary for OTAP, but, you know, you're gonna turn it into OTLP or some other protocol, it might just add up a little bulk.
So this is a very minor But very important.
distinction, it sounds like you could even make a, like, a Boolean flag that says, do you do it the one way or the other way?
That sounded even… acceptable?
**drewrelmas** 21:31 Yeah, I mean, it could always turn into a big, but I mean, it's a little…
For such a small thing, I'm not sure if it needs to be user config, but if that's the best way to do it, we can.
**Joshua MacDonald** 21:44 I would also support just doing what the Go Collector does, since that's what I think you're after.
**Utkarsh Umesan Pillai** 21:52 Yeah, that's what I was gonna ask, like, what does the GoCollector do if, there's… if there's a tag…
**drewrelmas** 21:58 Correct me. I believe that the gold collector from my testing
never produces the tag attribute. It always sets… it always sets app name, and if proc ID is there, it sets proc ID as well. So, I'm…
I'm fairly certain it always assumes… it always sets tag as app name. If you scroll up.
you can see, the second code block there, it says out.appname equals SM.tag.
**Utkarsh Umesan Pillai** 22:28 I see.
**drewrelmas** 22:31 And in the syslog receiver, there's no concept of…
syslog message.tag. It's only .appname and .proc ID.
**Utkarsh Umesan Pillai** 22:43 And they don't even have a field for content, like…
Because I see similar code for…
**drewrelmas** 22:49 I think… I think they turned that to message, if you scroll up, Josh.
At the very top.
**Joshua MacDonald** 22:58 Oh my god.
**drewrelmas** 22:58 That, yeah, they say… They, they treat it as message.
**Utkarsh Umesan Pillai** 23:05 So, in the code snippet below, I see a message has its own if block, but…
a content, if there is a content present, then it gets set as block ID, that's what it looks like.
**drewrelmas** 23:16 So, I think perhaps they're misusing the term content. I think in this parser implementation.
the content is what's in between the brackets, and message is what comes after, which should really be the content, I suppose, based on the RFC. So, I think that this is a little confusing internal parser implementation.
**Utkarsh Umesan Pillai** 23:39 Yeah.
Yeah, okay.
**drewrelmas** 23:47 My end goal is I would… like, my use case that I'm looking for supports app name and proc ID on RFC 3164. So at the end of the day, that's what I'm looking for.
**Joshua MacDonald** 24:04 Alright. This issue is… a little too low level for me at this point. I accept any solution.
It's a little weird, I'm gonna be honest.
With all these RFCs and having undefined behavior, but… or ill-defined behavior.
But, they all sound good. We'll just do it. We'll do it right.
I hope that's okay to move on from.
We can sort this out, I believe.
**Utkarsh Umesan Pillai** 24:31 Yep.
**Joshua MacDonald** 24:35 All right, then we come to my issue, which will also touch on a couple of open PRs, which I think now is probably a good time to discuss.
And others…
etc. Okay, so, Drew, did you put this hygiene, not urgent labels, and tag usage? Maybe we could talk about that first.
**drewrelmas** 24:53 Right.
Yes, that was me. I was just…
having… you know, there was an internal discussion with someone, here at Microsoft, and I was just looking at our issue list in general. I know we're at 179. I was thinking of ways we could…
improve not only our labeling, hygiene, but also making it easier for new people to come in and start contributing. Specifically, like, how we use the Help Wanted label, as well as the Good First Issue label.
And Tom, correct me if I'm wrong, but I think…
My understanding was you were kind of interested in trying to fulfill some of the triager roles, which we don't actually have an issue triager in Hotel Arrow yet, so this could help us out a lot. Mainly, I'm looking to…
you know, we have a backlog of 179. I see we even have a bunch of issues from…
The going days.
Rust's.
**Joshua MacDonald** 26:00 Yeah, yeah, there are some old ones in there that.
**drewrelmas** 26:02 Yeah, I would say.
**Joshua MacDonald** 26:03 work.
**drewrelmas** 26:04 I was closing. Just closing. Closing. Right.
So, I have a few ideas, like, I'm obviously a good first issue, I think we should treat as something that someone with very, very, very little context can come in and handle, but I also think Help Wanted is a good one we should try and use.
**Joshua MacDonald** 26:26 Where…
**drewrelmas** 26:27 it… it's something that someone could come in and handle, like, with help from someone else in the repo. So, like.
Given advice from a maintainer, or an approver, or someone like that.
**Evan Torrie** 26:41 I'm in the middle of a meeting.
**Joshua MacDonald** 26:43 Yeah, I agree. Yesterday, for example, Tom reached out to me and said, hey, Josh, I'm thinking of starting this issue.
Is anyone else working on it? And it would also be nice to be able to just go grab an issue and not have to, like, check in with a bunch of people, which is, you know, I'm glad he did, but, and we should have our issues in a better state if that's the fear. So I definitely would support,
Adding triageers. We do have a formal role, if that's…
you know, like, if it's repository permissions, we can solve that one.
so yes, I support… I support this idea, Drew. Maybe you and I could… Collaborate on a plan.
Or, .
**drewrelmas** 27:31 Yes.
**Joshua MacDonald** 27:31 Who's gonna do what type of planning?
But I think you're right. We have probably twice as many issues as we need, and many of them will not make any sense to anybody, and those are not helpful for anybody. So,
But it would be awesome if… if…
when I… when someone asks for an issue, and they say, I think I want to do this one, and then they get blocked, they can easily find another issue.
so, so yes, absolutely support.
And that could be any of us. If you're interested in doing that work, ping me as well.
Okay.
I… I will do my best now. I don't need us… we don't need to prolong the meeting any more than necessary, but… so I just showed you an open issue, which I filed yesterday, to kind of describe some of the overall steps that are being taken.
And I would include in that umbrella, a PR draft that Andres put together 3 weeks ago, a draft that I put together 3 weeks ago.
Laurent's been putting up telemetry guidelines, which are more to steer himself, as I mentioned, metric instrumentation for the pipeline components.
But it's a… it's also just a document on how we instrument in this repository.
And then,
this one here, which I opened yesterday, and I'm hoping we might talk about a little bit today, because it's,
potential… it could potentially confuse people where we're heading. So…
After that PR and the need and the issue, I did file this architecture document that I've, had, and,
This is a plan document for how we will do logging, and of course, there's so many questions that come up. And I,
Obviously, logging is… there's a million ideas about logging. We've all gotten into this field, probably because we have feelings about logging.
Working in OpenTelemetry, you can't not have feelings about logging. And…
the situation in Rust is rather unique as far as OpenTelemetry, and there's this sort of… every language has a different problem, or different, sort of.
situation on the ground when it comes to logging. So, we're looking at Tokyo Tracing because it's dominant in the ecosystem, and that's pretty, pretty clear, and OpenTeometry Rust has a, sort of, plays nicely with Tokyo Tracing because it's, hard to imagine replacing it, or,
superseding it.
And it's pretty well developed, as a first-class idiomatic logging API.
So to use that framework in our application, which we've so far resisted, requires understanding that the framework is heavily based on the use of sync and send traits, things crossing thread boundaries, and that we have
Thus far, really tried to not do that, and that's the reason why we've dragged our feet.
So…
it's like I've been waiting to do this for my whole career, maybe? I don't know, but I've been involved in logging libraries in the past, and this presented to me as an opportunity to do something that I've wanted to do for a while, so I will say I'm excited about this.
The… the… and I… now I just want to take you to the PR, because this document is… is describing… this is my… my first step in that PR… in that document is this PR here.
And…
what I want to bring out is that the architecture document lays out sort of two paths. There's the old way you did it with Tokyo, if you're a third-party library instrumented with Tokyo Library logging calls, we're going to support you.
there will be threading happening. There will be multi-threading, and there will be locks. There will be buffers that are shared, and there is a possibility for contention over logging if you're not careful, and we accept that. However, for the components of the pipeline.
which are sort of first-class elements of the collector, or the pipeline, the data flow engine. We are going to
have a logger provider or a logger object that we construct and hand to the components. This is where we'll insert our scope information. This is where we'll insert our thread-per-core logic to avoid contention. This is where we'll essentially integrate logging directly with our own pipeline.
if I haven't said it clearly enough, the idea here is to build an SDK for logging that does not
go through the ordinary path, it goes straight into the OTAP Dataflow engine, so that we will be internally consuming our own logs. Now, there's some safety issues there, and that's what that architecture document is about. This PR here
is, the first step, and I'll just sort of briefly talk through the highest level idea here. Highest level idea here is that translation costs are what kill us when we log.
Translation costs, basically, are to be avoided.
And the danger is that we… we just don't want to create too many intermediate copies of our log. So, for an OpenTelemetry project with an OpenTelemetry pipeline, with this project, with our… we have two data types in our pipeline. One of them's OTAP records, one of them's OTLP bytes. For me, in this project, the most natural
fastest, simplest logging code that we can find is to go directly to OTLP Bytes. And that means writing a custom encoder. It starts with the Tokyo tracing event object and ends up in bytes.
I did it two ways, because there are at least two code paths that are important in this… in this world, and it's, I think, important to always optimize your logging. So, there's two inter… there's an intermediate representation that I've developed here.
And I can just sort of maybe step into it.
The intermediate representation is…
So, people… okay, this is why I don't like putting… mod.rs is the right way, never mind, sorry. Self-tracing is…
**Evan Torrie** 33:57 It's.
**Joshua MacDonald** 33:58 part of this self-tracing directory.
**Evan Torrie** 34:00 That's true.
**Joshua MacDonald** 34:01 And the big idea here… oh my god, my mouse is not behaving me at all.
Okay, so I can't… there we go. So the big idea here is that we create a log record. This is the sort of, like, lightweight copy of a log event.
It has an identifier which refers to the metadata. So, Tokyo metadata is static information. It has call site, like, file and line, module, event name, stuff like that.
Timestamp is not included in the event. Tokyo doesn't take a timestamp for you, you have to do that yourself. And then the body and the atchers are encoded as OTLP bytes, so what we do is we have a partial OTLP encoding. Partial?
And I did it as little as possible. The point of being partial and doing as little as possible here is that we may not actually
log this. We might sort it before we get logged. We might send it to a channel for someone to consume, and it's nice to keep the timestamp in a primitive form, nice to keep the call site information in primitive form, because it's cheaper, but because we might actually use that information before we do output the data.
So, the reason why body and attributes are serialized is that those have a lifetime in the event. You have to capture the event fields before you return from the event. So this is how I do that. Capture them as OTLP bytes.
Okay. Now, the rest of the code, I don't think we should step through it, but we already have protocol buffer code handling in the codebase. I reused it. We also have code for reading protocol buffers as bytes directly, called views. I reused it as well. So, in this…
module here, which is… well, you can see OTLP bytes is sort of the theme here. The formatter module takes the intermediate representation with timestamp and metadata and encoded bytes
And then it uses the view to read the bytes and print the message. So what I've done here is implement raw logging. I say raw in a sense that there's
There's no channel, there's no buffer, it's just going straight to the console as fast as possible. Of course, the console will have contention, so this is not meant as the final story for us. This is meant as the encoder that gets us the efficient
towards where we're going.
**Evan Torrie** 36:13 So…
**Joshua MacDonald** 36:15 I stopped here. It's raw logging, there's no mutex, there's no cache, there's no buffer.
There's no intermediate representation. It goes straight to bytes and then straight to the console. I guess intermediate is bytes. So that's what I've done. I don't think we should step through the nitty-gritty details. The README kind of says exactly what we're doing.
The, and I'm… if I may, I think I'm going to invite Andres to speak, because he's got a draft that does something similar. The… as a user, what you're going to see here
And this is subject to change. Right now, the idea in my PR is that we have a service telemetry block that's the same looking as the Go Collector. Inside of that, we have the declarative configuration for open telemetry right now. And what I did for now, which is open to debate, is add this internal section to say.
Bypassing OpenTelemetry's configuration.
**Evan Torrie** 37:08 Good thing, Richard says.
**Joshua MacDonald** 37:09 Evan, can I… can I mute you?
**Evan Torrie** 37:11 survey.
**Joshua MacDonald** 37:12 I just need to press it
Anyway, the idea is when you set internal enabled true, we just go to this new path. If you don't set internal enabled true, you go to whatever we were doing before, which is to use an OpenTelemetry subscriber.
to format OTL… to present the OpenTelemetry SDK, as well as, I say, as well as meaning in addition to the Tokyo tracing format layer. So the Tokyo Tracing Format Layer is what used to write to the console. So when you say internal enable true, we bypass the Tokyo console logger and use this new thing.
My next…
work, if we may, on this, is to continue with these OTLP bytes, and then talking about thread local variables, talking about buffers, and talking about getting straight into the OTAP pipeline. That'll be the next step.
Andres, any words or comments or feedback, or discussion points?
**Andres Borja** 38:06 Yeah, I think I… I, grappled to the…
to the PR itself, but,
One of the questions is, why passing such a raw and unstructured thing as bytes instead of…
If that is using the…
line protocol that we are using in this case, I think it should be something top, I guess?
So… because if it
decide just bytes. I don't know what is even the format of those bytes at that point, right? So, why not pass in something more structured?
**Joshua MacDonald** 38:47 The… the… I have… my answer there is to think about the memory allocations that are going to happen. So, as I mentioned, the… the… when the Tokyo event happens, what you're given is essentially an iterator that can iterate through these lifetime event fields. You have to capture them somehow.
Now, you could imagine capturing them in, like, an array with key value, key value, key value.
But those values are still…
going to be enumerated types, so you could have a string, or an int, or a bool, or a double, or whatever. When it comes to that string, what are you going to do? You have to copy that data somewhere.
And that's why the OTLP bytes representation makes sense, is I'm going to build one vector of bytes, and I'm going to put everything there, so it's one allocation, or it even can be done on the stack.
As opposed to having to sort of copy each object, which would require some degree of allocation. The Tokyo interface also includes this Rust
debug struct, or inter… sorry, it's a trait. The Rust debug trait
is very sealed. You cannot destructure it in any way that I've been able to figure out. So, once you see this debug trait, it's a dynamic trait, impulse.
you have to do something with it, and the best thing I could figure out how to do is turn it into bytes. So, for strings and objects, the best idea I could find was to put them all in one byte array, as opposed to a bunch of byte arrays, or a bunch of strings.
Moreover, you know, protobufs are something I'm extremely comfortable with, but I want to convey that, like, a partial protobuf is still a protobuf, so when I encode those body and attributes fields as OTLP bytes.
They are just a protobuf in a standard representation. I can parse them with my other protobuf parsers. I'm using the OTLP view struct for zero copy. I parse through those bytes and reconstruct
The formatted representation, for example.
But I think the bigger answer, if I may, to the question is that, you know, we have
the OTAP data flow engine takes in OTLP bytes, and it has constructors to get from OTLP bytes to OTAP records through those same views. So, there's a sense here in which we can… what we're doing is enables an optimization.
And if you think about it, if what you're doing is buffering log records, and you have, I don't know, 100 log records, if things are happening quickly, now you want to output those 100 log records to a pipeline. We should be able to combine them into a payload. When you think of the OTLP payload, it's 3 levels of nesting.
You've got your resource, which is its constant here, but then you've got scopes, and if you look back at Laurent's document, there is a plan here that each component has its own scope. So somehow, we imagine that when the event happens, you can also figure out who's my scope.
Once you have that.
stored in addition, then what you could do is when you see your 100 log records, you can sort them by scope, and then you can construct a single OTAP payload that is scope-by-scope grouped, and that will be a more efficient representation. And then what we can do is pass it to our OTAP conversion.
we should be able to do a zero copy from zero… from the OTLP bytes to OTAP, is what I'm trying to say.
So…
**Andres Borja** 42:09 I guess my answer… or TLP bytes instead of just bytes.
I mean, I'm not…
**Joshua MacDonald** 42:16 I have… I've tried to say OTLP bytes everywhere here. These are always OTLP bytes.
**Andres Borja** 42:21 It's an object called bytes, it's not called OTLP bytes, so I don't know.
**Joshua MacDonald** 42:25 The object called bytes is the low-level data type in Rust. I don't even know where… there's a Rust crate called bytes. It's a buffer for bytes.
**Andres Borja** 42:34 Right, can we just not create a wrapper for that?
**Joshua MacDonald** 42:38 Wait.
**Andres Borja** 42:41 So we know that it's not any bytes, it's an OTLP bytes.
I'm not… I'm not questioning that we… that the zero copy, I'm questioning that…
We should send something that we know more what it is.
**Joshua MacDonald** 42:57 Okay, well, I mean, I… yeah, okay, so…
I could see a type alias or a struct that would add a little overhead, like, just more code. I don't know if I see a great benefit, but yeah, I'd be willing to call these OTLP bytes, and we could make an alias for it.
**Andres Borja** 43:14 My father… Relatively related, comment is… is more about
the usage of external libraries, right? So what we are doing is…
it's more like an abstraction layer over the different elements, in this case, logs, right? So…
So if we have control over that, the final destination is… it can be anything, because
You could argue that it's very popular, but… There are other frameworks, whatever.
**Joshua MacDonald** 43:47 Yeah, I agree with you, for the record.
**Andres Borja** 43:50 So I don't think we are kind of, like, interested in the telemetry, in this case, of the logs of…
A library that might be or might not be using
a specific thermal library, you know? I think we are more interested for this path of internal telemetry.
Okay, I…
**Joshua MacDonald** 44:08 I take your point, is that we don't really care about those third-party libraries of logging, maybe. Yeah. I really like the data fusion logs, by the way, in the same framework. So, but I did have that same position. You know, I created this type called save call site, and CJ asked me, like, what do you need that for? It's the same as the metadata. Yeah.
I make the metadata… put the metadata inside the saved call site, because I wanted to hide it, because I'm not convinced that we're going to pass Tokyo metadata every time.
to our formatter. Like, I think you should be able to get events from somewhere that's not Tokyo. So for now, I put this pointer to the, you know, ref to share metadata reference, because it's static and constant.
but I… but I put it private, and I… and I made accessors for all the fields that we use, so that we could…
I agree with you. Tokyo is not…
our only choice, and we need to instrument our components in a very, bespoke way, so that calling it Tokyo is, maybe a distraction. So I think I agree completely.
**Andres Borja** 45:14 Right, so I guess…
My suggestion is, let's start with the use case we are trying to implement, which is, yes, this transformation, it's amazing how we deal with that once we create it.
But, you know… If the destination is gonna be something like…
Tokyo Tracers or something like that, sure, that should be our destination, but not… it shouldn't be the,
the intermediate layer that we should be coupled to, you know? Yeah, the intermediate layer…
**Joshua MacDonald** 45:46 point is partial OTLP bytes and structural fields, and I think that, I think that's providing the requirements that you have.
Yeah, I just don't want to downplay the idea that Tokyo Tracing is widely used. It's used in many components you might not even realize. It's used in the HTTP library, it's used in the gRPC library, and if you're debugging, if you're developing, if you're diagnosing situations, you're going to want those logs. You're going to want to add your own logs, and those are going to be in places where you don't have access to
the framework. You don't have access to your event handler Or your effect handler.
you don't have access to the data flow engine, you're just off in some code with no context. Now you're going to use Tokyo Logging. It's the only solution, short of a different SDK, which we don't want to invent.
Well, I'm afraid that we've now beaten this topic quite a bit.
This is my first implementation,
PR, and I was planning to… the arc here is that we will end up being able to consume our own logs one way or another. Many details are to be determined, but the final goal here is that we can safely be the SDK
Without an OpenTeometry SDK. And that's not to… to sort of dismiss the OpenTeometry SDK, but this is an OpenTeometry project, this is an SDK, this is just a new SDK that's built for a Rust pipeline.
That can consume its own telemetry.
And, you know, I think we might end up influencing each other. Like, we would be able to use more of the SDK features if they could accept OTLP bytes directly, for example.
And, this, I think what we're seeing here is this is performance competitive with the current
open telemetry implementations.
Even for OTLP, which is probably, you know, I would say we're gonna outperform the OTL SDK and OTLP quite a bit until what I just said could happen. OTLP could deal in… if the OTL SDK could deal in bytes.
We would be in a better place.
I don't… I think that we've probably lost the room here now, and I'm gonna propose that we're done with this conversation,
Oh my god.
My mouse is totally misbehaving right now, so that's what I have to say.
Well…
Well… people.
Does anybody else have anything that they would like to bring up in this?
In this meeting.
I won't force you. I love it when we end meetings early.
So therefore, if no one says anything, I'm gonna propose that we did it. We did it again. Thank you all. Next Tuesday, there'll be another meeting.
You can see me on Slack.
on Teams… Send me a PR.
Thank you all.
Cheers.
**drewrelmas** 49:02 Oh, buh-bye.
**Pablo Baeyens** 49:04 Thank you, Josh.
**Utkarsh Umesan Pillai** 49:05 Thank you.
