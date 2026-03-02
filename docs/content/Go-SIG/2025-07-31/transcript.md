SIG: Go SIG
Date: 2025-07-31
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/R0HM58kzsx7N7MPAqn6z4kANwELimz6JWtM8nyERpKdqZ9Glx1zn7IUJBCudrR3r.CA6dL1p8gMWeBp3j
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:16 Hey! Brian.
**Bryan Boreham** 00:19 Hi! There! Hi! There! How's it going.
**Tyler Yahn** 00:21 Going? Well, how are you.
**Bryan Boreham** 00:24 Pretty good, pretty good.
**Tyler Yahn** 00:27 Yeah, chugging along right.
**Bryan Boreham** 00:31 I was. I was just looking at my list of things to do not so long ago, so
I'm depressed.
**Tyler Yahn** 00:40 Yeah, if your list of things to do actually like is static, I feel like mine's like a leaky bucket implementation like it just always is adding things and never fully complete. Everything so.
**Bryan Boreham** 00:51 Yeah.
**Tyler Yahn** 00:52 Yeah, but yeah, it's the way
the way the world, I think, eventually gets to.
Yeah, I don't know how many people are gonna be joining today.
I know Robert's not able to make it, and Damien doesn't normally come to these. But the other 2 Maintainers are likely going to be here. But if you haven't, yeah, go ahead and add your name to the attendees list.
and then if you have agenda items you want to talk about. You can add them there, and we can wait a little bit
for others to join.
**Bryan Boreham** 01:30 Yeah, I I I only recently started attending. So I don't really know.
I I might be a little bit interested in talking about Protobuff, and performance.
**Tyler Yahn** 01:49 Okay? And this, specifically, is in the the otlp, like exporters. Right?
**Bryan Boreham** 01:56 Marshalling and unmarshalling.
Otop in go the agenda.
**Tyler Yahn** 02:08 Sure. Yeah.
Sounds good.
Hey? Sam.
**Sam** 02:19 Hey! David!
**Tyler Yahn** 02:22 How's it going.
**Sam** 02:24 Good.
How about you?
**Tyler Yahn** 02:28 Yeah, doing good doing good.
I think this is probably gonna be
it for the day. Maybe David will be able to join in a little bit, but maybe not.
So yeah, I guess we can jump in here. If you have agenda items you want to talk about.
go ahead and add them there to the agenda, and then, if you have, or if you haven't, did already add your name to the attendees list, but looks like everyone's there.
Okay, stop. Zoom.
okay. So 1st up, I wanted to check in on our hotel earned milestones. So let's see if I got these right?
Yeah. So I wanted to like, there's a few things definitely still in progress.
some of the bigger ones are this cardinality limit. This is kind of blocking the release. So it looks like there's been progress on the apply cardinality limits to aggregation. This Pr looks like it's is this in the milestone. Now.
it looks like it's progressing is approved. It just needs, I think,
to wait for a full day. I think. So. Yeah, that looks like it's coming along.
I think if there's follow up work with testing and then
deprecating and fixing other things related to the cardinality stuff. So this is still, I think, the main blocker. But progress looks like it's happening.
Let's see
also on here exposed client interfaces for Otlp metrics. This is something that was, I think, brought up a few weeks ago, and I added it to this milestone as maybe something that's useful. So
yeah, I think this is like one of those things where we probably just need to come up with some ideas. If you have ideas on how to complete this.
please take a look. So this is just asking to support some additional protocols. So another option or one option is to support, like
registering a client similar to what we do for the tracing setup. Another is to just provide the translation functions so that other people can do this translation on their own.
I think Robert was in favor of the translation approach. If I remember correctly.
which seems fine, it's not the 1st person to ask for this as well.
We would probably want to do this more holistically across all of them.
all of the exporters. So I think that's probably what we want to go do. If we're going to do that.
I think we've always said to just copy it. But
yeah, I think it just needs more, some more. So I don't know if this is going to be included in this milestone, but at least actually, it probably shouldn't get included. Because we don't really have a clear vision on this. I'm going to move to the next one. But yeah, if you have interesting
or opinions on this one, please go ahead and comment on this issue.
Maybe start from the top here. Okay, so address issues with open telemetry. Cll Monitor, this is something that I think we can still continue working on. I think this has gone pretty far.
The dependency policy and the open Ssf security insights manifest. These are things that are pretty straightforward. If I remember correctly.
I was looking into this before a break a while ago.
but I don't know exactly. I think this one just needs
to look at the documentation on it like that. I don't think it's actually too complicated. And then this dependency policy.
Yeah, I'd have to look at this one again. But I think that this one might make sense to not do in document, that we're not going to do it. But I can't remember exactly. But yeah, these still the ownership
people to actually address them. It's something that I'm possibly going to be coming back to in the next few days.
Try to take a look at this and get it resolved. But if other people are interested in trying to resolve these, these are good issues to try to get done for this milestone.
Actually, I don't know why these aren't also included in this milestone.
Okay, except I've got a Pr for flattening the bridge of telemetry internal packaging. So this is something that is
stalled. It looks like.
I guess the username's not gonna pop up. Okay, I'll let Nardo.
I don't know. Yeah, I don't see definitely don't see Leonardo on here. So
it looks like there was a request from Damien to update. This
looks like it's been updated looks like tests are failing. It looks like it needs to get synced as well.
Why did this fail?
That's kind of weird.
Okay?
Why am I not able to restart this.
**Bryan Boreham** 07:41 The issue that it was supposed to fix was closed by 6, 9, 1, 6.
**Tyler Yahn** 07:53 Thanks for pointing that out. So flatten the bridge.
Okay, so if that's the case, then we could probably close this
perfect making progress.
Okay, trace add on Marshall functionality to this man context and subfields. I think this is one that I was trying to think through.
We originally had been asked to add, add Marshall Fields to here. I
think that it was one of those things that we didn't want to do, because, providing this functionality enables, I guess, what we would call a foot gun, something that allows users to do some interesting span propagation where you probably want to be using a span propagator instead.
So I think was right. The initial asked.
Do this wasn't actually supported. This is being asked again.
So I think it needs to, I think, get reevaluated and determine. If, like, this is something we want to support.
It doesn't have, I think, any reviews outside of Damien. So it's looking for for more reviews at this point, if I'm not mistaken.
Yeah.
yeah.
that's a good point. I think that what this is going to do is actually introduce a format for what this
trace context should look like I don't know.
Hmm!
I think it's providing just the unmartial this. So I don't. I don't know if that's actually the case. Looks like the unmartial alone should be.
Hmm, although I guess it also is providing the Marshall.
Yeah, I think we need to think through this and find out if this is actually what we want to do. I think things like
you know, like our field names can't change if we are going to just directly do this is remote, becomes an exported field. In effect.
even though it's not syntactically, it becomes something. You know this field name can't change
which is a little bit troubling. Given that like, we've put a lot of effort into trying to not expose these kinds of things from the internal representation.
So I think we probably want to pay attention to this.
But yeah, okay, so this needs, I think, review for this milestone
also on here, this trace, optimizing, id parsing and string functions also unreviewed. At this point.
It looks like there's benchmarks. It looks like there's linting issues.
I don't see any fix for the linting issues, though.
Yeah, okay.
so that looks pretty straightforward. It's like, say, it needs line wrapping. It also needs to be updated.
Okay.
deprecate and rename the Schema X types package is a proposal that was provided by Damien.
So it looks like this was ignore schemas.
Yeah, I think this already got
addressed where we are just ignoring this.
Yeah, I think there's definitely some.
The schema, I think package is kind of
it's been abandoned at the specification level for the idea of entities. So
I'm not particularly motivated to work on this. Given
like, there's not a lot of support in stabilizing this at the specification level. So I'm not too sure we'd really want to spend too much time on this. I don't know if this is actually like needed.
This
proposal here is, I mean, I think this is just moving things where it works currently. And we're ignoring the issue. I don't know if there's really much
value in us addressing something that isn't actually used.
I
I don't think it needs to be included in this milestone, I can move it to the next, at least.
Okay.
Fixed callback. Error. To not return is another pr, that's been open for a few weeks. It looks like
there's definitely some follow up that's needed.
I don't see any follow up actually being made here.
Yeah, it doesn't look like there's a ben follow up. I think that we could probably close this. We might wanna
track this as an issue.
because it does look like something that needs to be done. It just doesn't look like there's been any movement on this. So I think maybe what we'll do is we can close this
and instead track it as an issue.
I don't know. I I can do that after the fact. Yeah, I'll try to remember
this.
Okay?
Then we're back down to
the cardinality limits components which we've already talked about. This is something that's just a work in progress. So I think that that's an overview of the milestones work to be done. So there's
work on the clo. There's definitely some review that needs to be added here.
I don't know why this is still here.
There we go.
Any other things that people think should be included in this milestone that aren't included here, or
things that are included, that we want to talk about.
If not, we can jump into the contrib milestone as well.
So
the minsev let's start up here. So they removed the deprecated stream client interceptor function from Otl, Grpc.
Got an assignee 3 weeks ago. I think I'm going to. I haven't seen a Pr. For this
where
no, I don't see it. Pr, okay.
okay. And then also similar here. I don't think that there's been any movement on this
oops.
No, it doesn't look like it.
When was this assigned?
Okay, perfect.
I imagine that might also be the case for the stream climate interceptor as well. We probably want to double check that this isn't already done.
But yeah, we can do that. And then the minsev severity and severity bar should implement the string related interfaces. This is a proposal. If I remember correctly.
I don't see why this wasn't
Okay, so this might be something that they're still working on this.
Okay.
I think that's it. So with that, anything else in the contribute repository that people wanted to include or discuss related to this milestone.
If not, I think that that sounds good. I think we have a plan. There's still work, plenty of work to be done for all these things.
But yeah, I think we'll have to keep working on it. We're definitely not there yet. And so yeah.
we'll we'll check in again next week.
Okay?
moving on next, Brian. You want to talk about the performance of marshaling and unmarshalling Otlp and go? Java has some hand optimized codes. has.net. How about go.
**Bryan Boreham** 20:46 Yeah, I just wanted to bring it up. And but kind of test test the temperature.
I I'm kind of passionate about making things go faster.
That's my Hopi and the.
I mean, it's it's kind of well known amongst people who work with protobuf that that the standard, Google tools
don't help.
Yeah. So I mean, has this been discussed before? Is is.
**Tyler Yahn** 21:29 Yeah, it has. There's there's definitely been. It's been recognized ever since we started using Otlp.
which uses these Protobuf libraries that we may want to support this.
It's something that was looked at. But it's also, you know, something that was
taken under the understanding that, like once you start doing custom
marshaling and unmarshalling of Protobuff messages like you are now in control of that, and you you are now responsible for it, meaning that, like any updates from upstream like, it's not something that you know. You can take advantage of them if you back, port them, or if you move to to utilize that. But that development capacity hasn't been there. So like, I think if you're willing to
take on that ownership responsibility, I think that that's something that we could look into supporting. It wouldn't be, I think. What you're you'd be looking for is in the proto. Go repository if I remember correctly.
But
it maybe not actually. But anyways like I would look at that repository as well if you haven't yet to find out. Maybe that's because that is like a more of a centralized location.
If you are, I see a confused look. Maybe I can also share my screen if you want to see the repo
**Bryan Boreham** 22:49 Oh, yeah, I was just wanting to refer back to the
something which I seem to have closed the tab.
**Tyler Yahn** 23:03 Yeah. So this is the centralized place for Otlp. This is where a lot of the protobuf implementation is is generated from obviously like
using tooling inside of the collector, and inside of our exporters exist as well. But this is like the generation spot. So is this what you were talking about?
**Bryan Boreham** 23:22 Well, the code that shows up in my in my profile is in is is imported from go dot opentelemetry dot I/O slash collector, slash p data, slash, internal slash data, slash, protogen.
**Tyler Yahn** 23:35 Yeah. So that's gonna be in the collector. Then so.
**Bryan Boreham** 23:40 It's in my program. But for whatever reason it's linking that.
**Tyler Yahn** 23:46 Well, that comes from P, data is the thing. And so yeah, that's definitely something sorry. What was it? Was it internal? Or was it just P data? I think.
**Bryan Boreham** 24:00 It's go to opentelemetry dot I/O slash, click! I could. I could probably copy, paste that into the chat.
**Tyler Yahn** 24:08 Okay.
**Bryan Boreham** 24:10 I click the right button.
Oh dear,
give me a give me another second.
wow, I can probably
where is chat chat is here.
No, no.
So that's
the past. From wherever that's the import path that it's using.
**Tyler Yahn** 25:08 Yeah.
**Bryan Boreham** 25:09 Well, I guess it's not important. Maybe it is.
**Tyler Yahn** 25:13 So yeah, I mean, it's definitely coming from the collector. So like, this is, this is definitely.
I think, going to have to be discussed with the collector, because this isn't something that we own. Actually, whether they'd be interested in looking at refactoring this, I don't know what specifically you're proposing here, but
I'm guessing it has to do with these unmartials functions here.
**Bryan Boreham** 25:40 I am not really. Yeah. I'm not proposing anything. I
kind of looking for pointer. If you say it's been discussed before. Is that written up somewhere.
**Tyler Yahn** 25:57 No, it's only been discussed in the sense that, like when we introduce this is in. This is in this Sig. We've discussed it by using like the otlp
sorry I don't know where.
I guess it changed. So it's in the proto go library. We've discussed like writing custom on Marshall, or custom like deserialization and serialization protocols that would be more optimized for this. It was just in in conversation here, but it was always kind of just one of those things that
we we recognize. It could be possible.
from the collector standpoint like this. This specific thing I don't know. This is a different sig. This is a sig that would meet.
let me see, I think they meet later.
Nope, I have no idea where the collector Sig is actually used to be later.
yeah, I don't see it. Maybe it's like every other week.
Sorry. I'm trying to find it in the calendar.
**Bryan Boreham** 27:04 It's it's fine. I I probably have a a colleague who attends and
I just don't know who that is. After. Jurassi left.
**Tyler Yahn** 27:19 Oh, yeah, yeah, there's like an 8 pack one. So yeah, I don't. Yeah,
I'm sure I'm sure you do as well. I just I don't know.
yeah, I you'd have to ask the collector specifically if they've had that conversation before any any. I mean, I I don't.
I imagine it's yeah. There you go. Thanks. So Tuesdays, it looks like, yeah, so
yeah, that's why it's alternating. And so I think that like the the answer is probably going to be the same from them in that, like
it, they they also have a lot of
To like
a lot of code to review a lot of code, to contribute a lot of issues, a lot of Prs, and not that many contributors for that amount. So the developer like capacity to handle this kind of stuff is going to be limited. So again, like, I think, if it's 1 of those things where like, if you came
with the understanding that, like, that's your plan. You plan to maintain that sort of like code base and that sort of like
optimizations. I think that they'd be more receptive to that. And I think that's the same is true here, like, if if you found
ways to look into optimizations like that makes a lot of sense as long as like you're you're willing to to take on, you know, when Prs get opened
for bugs or security issues or features, or something like that being able to review them, being able to like collaborate on them.
I think there's a lot of openness to to increasing performance. I don't think anybody really doesn't want to increase performance. It's just the cost, right is is always the question of like.
**Bryan Boreham** 28:49 Yeah, no, it's it's fair enough. I? yeah, it's it's
I'd like to say, just kind of take taking the the temperature, because I
I don't know whether I mean I'm not gonna undertake
what you said personally, but my employer might, and and perhaps more likely, if we can get some kind of coalition.
going on. I mean, it's kind of one of our customers that that put me up to this. But I am interested for myself also. But yeah, so we we might. We might get
more than one company to commit, or or we might not. Yeah.
**Tyler Yahn** 29:43 Whatever
say is, if if you could get that, if you can get more than one company to commit, that'd be great, especially if you came and said, like, you know, it's not just me, or it's not just one of my colleagues, it'll be, you know, multiple people. I think. Also.
**Bryan Boreham** 29:57 Sorry.
**Tyler Yahn** 29:58 I think, also having a clear understanding of the scope of work like what you plan to address, maybe in like a phased perspective, but also getting some some benchmark numbers would be very helpful, saying that, like, you know, here is a you know, an area that I've looked in profiling. Here's an area that I've just done some quick prototyping. It can show.
you know, a 20% or 5%. You know, a 2% improvement in performance. In these these cases it justifies, I think, a lot of the the effort. I guess at that point.
**Bryan Boreham** 30:29 Yeah, so I I so it's very useful to know that it's actually a different sig.
I I mean
to be honest, I I find it surprising that that Java and.net are ahead of the collector in in this respect, because it's the thing that everybody uses.
**Tyler Yahn** 30:53 No, not really so. The thing is with protobuf is. It's a really well supported, I think. Language in go in Java. It's not like. Actually, I think it's like the the default. Libraries are pretty much unusable in Javanet. I don't know. I imagine it's very similar, but I definitely know that the imports of protobuf in the Java world are like a well-known thing that, like it's just something.
Then almost everybody just rewrites their own implementation because it's so broken.
So that actually makes a lot of sense to me for the Java implementation. the.net, I imagine, since it's so similar. Yeah, it would be close.
But yeah, and go. I think that there's a there's a you know. It's a really well established library in the Google space of what they've provided.
I don't think anybody is like claiming it's perfect. I think it's 1 of those things that like it works so generally that it works. And I think that's why it's been so heavily adopted. But yeah, like, I think that, like I have definitely seen, especially in internal companies that, like you find specific use cases that like that over generalization causes performance, you know, overhead.
And you can get, you know, on the order of, I don't know 3, 5% performance improvement if you change it, and it's worth it. Because, you know, at scale 3, 5% turns into real dollars, which I'm sure I'm not explaining anything new to you. But I think that like that makes a lot of sense. It's just that, like in the go space. It's 1 of those things that it's so widely adopted that you really have to have motivation for it.
**Bryan Boreham** 32:26 Okay, so let me go a bit further into into concept. So the
I mean the the code that you're kind of
enticed to use, takes the protobuff and turns it into a an entire
directed graph of objects, you know, basically a blizzard of tiny, tiny objects because of everything's behind a pointer, and
everything's in a slice and and so that's essentially what what shows up in in profiles. It's it's and
I would suspect that pretty much all of the time. Nobody actually wants a blizzard of tiny objects.
You know what you you're trying to do something with the data you're you're I mean, what we're trying to do is stick it in database. That looks nothing like
the way it came in. So so I actually suspect.
the the what would work best for us is he's a
a kind of streaming Api that that sort of walks through the data without, you know, the difference between like a a dom interface and a and a streaming interface. And
no, I'm in Xml. Sorry I'm in the lost millennium
but you know what I mean the the that kind of style of Api where you also get it with Jason.
**Tyler Yahn** 33:52 I think that is something. That is what the P data project was trying to, I think, accomplish actually.
**Bryan Boreham** 34:00 The witch, Purchase.
**Tyler Yahn** 34:01 The. It's the one that you're referencing this like, P data like, it's it's in the collector. It's it's there to try to like.
It's try to try to put these stitch these little objects into contiguous memory as but as best it can outside of your Protobuff representation. Obviously, and then, like the contiguous memory, can either be
not touched if it doesn't actually need modification that it can do a lot of these things outside of this, and then, if it does like modify things like that, tries to to make sure that whatever is modified stays as contiguous as possible.
So I think that.
**Bryan Boreham** 34:37 Very
interesting. I'll need to look at that. Certainly. The way our code is calling it does not achieve
what you just said. So.
**Tyler Yahn** 34:48 Yeah. So I think, like, if you have a use case there, I know Tigran, who's in the collector. Sig would be very interested in knowing about it. He's like
very much into the optimization of Otlp for use cases. So knowing your use case, knowing like what you're seeing, what you're not seeing.
**Bryan Boreham** 35:05 Prometheus, right, I mean, and I work on a derivative of that. But
It. It's I'm working with with David Ashpole that you might have come across.
**Tyler Yahn** 35:16 Yeah.
**Bryan Boreham** 35:16 On
What? What? So one specific case is is Prometheus receiving otop metrics.
Me!
**Tyler Yahn** 35:30 Yeah, I I think I think that's something right up Tigran's Alley. He'd be interested in understanding this this use case specifically, since it's so, you know, it's it's Prometheus, right? Like, that's a very
popular standard to understate things. And so like, I think, yeah, like, I think that's definitely something that I could see him, plus others in the community being interested in trying to find optimizations or trying to find formats to to work with this.
So yeah, I guess. Probably the answer is just like, yeah. The collector, Sig, would be where you'd want to talk with them.
I might recommend even just reaching out to Tigrin in slack prior to that, like in the Cncf. Slack, just because
I don't know how regularly he attends the the collector Sig meetings. But that's the person you want to talk to is Tigran. If if not, he'll point you to the right person. Yeah.
cool
**Bryan Boreham** 36:23 That's very useful. Thank you.
**Tyler Yahn** 36:25 Yeah, yeah, I mean. And again, like I, yeah.
he, he explicitly like added it so that it would do something along those lines and and work very well in the collector, so I imagined he'd want to try to optimize it as well for this. So yeah.
yeah, well, let me know if if you're not able to get in contact with them, I can reach out as well. And yeah, we can go forward.
**Bryan Boreham** 36:49 Sure.
**Tyler Yahn** 36:51 Okay, going back to the agenda. I don't see anything else on here.
We do have a little bit of time. Any other topics. People wanted to talk about.
If not, we can end the meeting early here. Thanks everyone for joining. We'll see you in a week's time, otherwise asynchronously. All right. Bye, everyone.
