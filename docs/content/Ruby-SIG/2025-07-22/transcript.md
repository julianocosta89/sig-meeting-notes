SIG: Ruby SIG
Date: 2025-07-22
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/yrId8jkxhMshq130dGq8PFPt_5H7ZWELiLe4ScWEsOb36sB5QphURzRRu_8MQer-._9JSaZdpN3_Kj_wa
============================================================

## Zoom Recording Transcript

**goutham** 00:14 Hello! Hello!
**Eric Mustin** 00:17 Howdy oh, you, we were talking on. You are over at Grafana right.
**goutham** 00:25 Yes, yes.
**Eric Mustin** 00:26 Yeah. Hi, thanks for joining the seg, yeah. Yeah. Yeah. Jaeger, Jaeger guy, right? Jaeger.
**goutham** 00:33 Prometheus, Yeah.
**Eric Mustin** 00:35 Right right. Maintain Prometheus, but you had a question on remote sampling and.
**goutham** 00:40 Yes, we want to.
**Eric Mustin** 00:40 Cool. Yeah.
Some folks will join usually give them 5 min or so, but.
**goutham** 00:46 Now it is.
**Eric Mustin** 00:48 Thanks for coming.
Are you still over at Grafana these days?
**goutham** 01:00 Yes, but I'm on a sabbatical.
yeah, I go back to work in 2 weeks.
What are you doing here? Go away. Go enjoy your life here.
No, I'm just kind of helping a friend set up doing some Sri stuff for a friend. So yeah, Ruby on rails.
**Eric Mustin** 01:17 I sounds like sounds like your friend is a smart smart person, then. Yeah, no, I I used to. I worked a bit with Jirassi, who left Grafana recently. But you you have a bunch of good folks there, so I appreciate you joining.
**goutham** 01:32 Yeah, yeah, I used to work with. I'm really excited for his new venture.
**Eric Mustin** 01:38 Yeah, it looks. I'm I she'd hired me. Yeah, I think it's cool. I think it's cool. I want to.
I wanna get smart enough about it to figure out how I can fit it into my own stuff. But I think it is
of telemetry is the right way to go, so it's cool to see it.
**Kayla Reopelle** 01:59 Hi! Everyone! Hannah is on her way. She'll be here in a little bit.
**Eric Mustin** 02:06 It's okay.
**Kayla Reopelle** 02:08 How's it? How's it going.
**Eric Mustin** 02:10 Just drinking from the fire hose of like new company acronyms, and.
**Kayla Reopelle** 02:15 Oh!
**Eric Mustin** 02:16 Insurance stuff and onboarding.
Gotta learn cabana. I don't want to learn cabana.
**Kayla Reopelle** 02:22 Yeah.
**Eric Mustin** 02:24 That's what the graphonics is for. Why am I doing this all over again?
No, it's good. Yeah, yeah, it's good. It's good. How? How are you?
**Kayla Reopelle** 02:33 Good. Yeah. You know, it's still kind of a slow start to the quarter. So that means there's lots of time for hotel reviews, which is great.
**Eric Mustin** 02:42 Enjoy it while it lasts. Yeah.
**Kayla Reopelle** 02:43 Exactly. Yup Yup, before they find out that.
**Eric Mustin** 02:47 All right, like I'm busy here.
**Kayla Reopelle** 02:51 I think we can get started.
so I can go ahead and share my screen.
Here we go alright. Can everyone see that?
Cool. So
I went to the specs this morning. There were a few interesting discussions the trace id based ratio has recently
like
gone stable or is going stable, but in a strongly refactored way to the point where, if it had already been implemented by a language, the new spect approach isn't actually compatible. And so there was a discussion about, you know, since the trace id based ratio was
was never really marked as stable, you know. Is it a breaking change to adapt it, to make it match the new specification or not. And ultimately, for user experience. The consensus seemed to be that
these changes that have been made we'll probably just get a new name. That's not trace id ratio based, and that is the thing that will get marked stable, and then the you know, currently existing one will be marked as deprecated.
So I think that's you know, not happening immediately. There will probably be more discussion for a little bit. But something to be aware of. The other discussion
that they had was around exceptions on laws.
There have been some discussions about trying to remove span events. And I think that recording exceptions is one of those sticking points about why span events should stick around. But there's
this idea, this proposal. To potentially record them using logs instead. Still in draft. So this is pretty pretty early. Pretty fresh.
was especially looking for someone to review this from a language that doesn't have exceptions. So I'm not sure if anyone is active in other Sigs for a language that doesn't have a concept of an exception. But
your your call has been made. And yeah, so I I haven't dove deep into this yet it was kind of just more of a discussion, but I do believe we record exceptions to span events right now. So if this changes. If they get pulled out, we might need to adapt
to this new spec.
But yeah, that's pretty much it. Everything else was kind of just.
you know. Please look at this. Pr, no real discussion.
Great. Okay. So let's just dive right in to core.
Oh, Shawn, I don't know if you saw I left some feedback on this. Pr, most of it's pretty minor, but just wanted you to know so that we could wrap it up and get it merged this week.
Eric, you want to talk about this one.
**Eric Mustin** 06:27 Yes, I definitely remember. Oh, this is just a heads up to Juan that
The folks over at adigos, who are
They wrote most of the Ubpf instrumentation. Go that got Eaton Fetterman. It's it's a nice startup, but
They appear to have referenced. Maybe some of your Pr and shipped their own auto instrumentation.
Which is fine.
But it's
just a heads up that they just announced it, and I saw. I just saw it come across. And I it occurred to me that we might get some an influx of
yeah, people going, hey? Why, their stuff is also kind of like a little flaky So
if stuff starts breaking or we start getting bug reports about our auto instrumentation.
it might be good to clarify whether they're using. You know our Pr upstream, or whether they're using this vendor specific
sort of like fork of our Pr which is not doing anything. Magic.
It's taking some of this. They they kind of just ripped the code out of the pr, and then just land. But could that? You know they're a small team. So they just landed it in their own repo.
and I think there's some
slight differences in that. They only support rails rather than some of the broader stuff that we support auto instrumentation on
but just a heads up that it could be a cause for confusion. Because, yeah, it's a.
It's a a feature that doesn't exist in actual hotel. But it's I know we're working on it actively. So anyway, I'm just was just pointing that out. It's a Amir. Amir is over there. He was, he wrote. Some of our the folks who wrote some of the aws instrumentations for Ruby.
who were at a different Israeli startup got bought by these guys. Or something, anyway.
that just came across my radar. So I was. I was surfacing it with no actions there really.
**Kayla Reopelle** 08:26 Thanks for sharing. That's a great announcement.
I feel like it's kind of becoming practice that, like our development, or like Beta, release, is just a a long lived pr, that people install directly as a gem, and then
we eventually.
**Eric Mustin** 08:40 Yeah.
**Kayla Reopelle** 08:41 Actually merge the pr.
**Eric Mustin** 08:42 Yeah, but yeah, anyway, that's all I got.
**Kayla Reopelle** 08:46 Thank you.
All right, Sean. Do you want to go next? Otlp, exporter.
**Xuan Cao** 08:54 Oh, yeah.
So first, st for the 1st one the feedback about the naming maximum or maximum I think the most common scenario, those 2
I mean I don't know, I mean for
I think the those name are interchangeable.
And Martin, they both are like
how they process like balance
word. But but anyway, yeah, and then.
yeah, today, I was doing the feature check because one of my work. You have to do this so just found, like 3 point that we think is missing. The 1st one is about this.
So we have a like a trace matrix log, and there's a profile.
I think it's they they put in in their spec.
so I haven't checked other language if they have implemented this yet, but
the profiling will be a nest casino, or the
for all the SDK, I think.
Yes, 1st thing. Second thing about Http version. So
again, I haven't checked out the language yet, but from the spec it's a
the Http 2 will be a default
if HP. 2 is not available, then it will fall back to the H. 51
But for the net Http, because we use net Http to make the request, and Http. Doesn't have the Http to support
the one option is using to Httpx or Friday.
Oh, yeah. And then the searching. I'm not sure if this
came up before it was the Json support.
Again. I haven't checked out other language but
prospect, you say he says we we it has a support post
for both binary and then the Json
currently we only support binary. No, Json, so
that is the reason I I found out from just looking at this
the spec, and then compared to our current information of the exporters.
Yeah, that's pretty much it.
**Kayla Reopelle** 11:24 Nice. Thank you for noticing and kind of diving into the missing features. Would you mind creating issues for those so that we can work on them.
**Xuan Cao** 11:36 Yeah, I will. Yeah, I will check other language implementation. See if they are already have. And then we can have a
I will, I will make the issue more more detailed.
**Kayla Reopelle** 11:51 Sounds good.
Okay? Any oh, one other thing with core. So we do have some
changes that need to be released for the SDK, and the logs. SDK, there has been some prs coming around for security purposes kind of related to changing permissions on the Ci.
The latest one just missed something that's blocking the releases right now, and I'm talking. I've reached out to Trask to make sure. He opened a Pr. With the fix, but it was in draft mode. So once we get that figured out we'll probably merge that and then rerun the weekly release. Request to get those? Ready to go.
Okay. Yeah. I guess. Eric, do you wanna start with Contrip?
**Eric Mustin** 12:46 Sure I'm got got I I is it? Pronounced Gautham.
**goutham** 12:54 Yes, you got it right. Got them? Yeah.
**Eric Mustin** 12:56 Okey dokey?
Well, yeah. So got them opened a or or commented on a very old issue that we had closed year years ago. Around Jaeger remote sampling which is, I think, a supported like it's optional in the spec. But
At the time. I think we had closed it because we didn't identify any. There was no one using it within
the there's no appetite for it just in the sense that, like none of the folks contributing, we're using it at the time when we were at shopify. We weren't. I don't think Github was, you know, new relict, whoever
and most folks were, were kind of in general, like moving off Jaeger. But it is a a valid, you know, like it is mentioned as a possible thing to support So
got them opened up a an issue, noting I guess 2 things. One is that there's a
sort of like a inherent, not I wouldn't say flaw, but maybe a limitation in some of in that in the way we do
that funky like. Let's start a span and rack, and then enhance it downstream and like a rails, or, you know, Sinatra, or whatever where. If you attempt to do a sample if you attempt to make a sampling decision
creation time of that rack span.
you're making it based on information which would then change in downstream so like, then you can't necessarily so. The span name you see in your ui or SDK comes from, let's say rails or sinatra. But when you go to attempt to write a custom sampler to maybe say, Hey, I want to sample out like those health check endpoint things. You're only given access to the information in in rack at the time. So it's sort of difficult to.
yeah, it's difficult to yeah. Make write a sampler, or perhaps impossible to write a sampler.
given that lack of information you have at sampling time. He also, and then also mentioned the benefits of like this Jaeger, remote, sampling approach, which would, I guess, allow us to
it, would allow those sampling decisions to be made via this remote sampler.
I believe. And then also we have some prior art from like the aws remote sampler that's being worked on. So yeah. He had mentioned that he would be interested in in one just like reopening the issue. And so there's a question of like, well, where do we move the issue? Kale I think you mentioned
contribute that makes sense to me. But you know, I guess we'll talk about here. And then 2 like, if anyone's interested in actually working on this
Jaeger, remote sampler, which you know I won't put words in your mouth, but it sounds like I can read them off your text. So it it does sound got them like you're interested in in contributing working on it, which is great.
And then I guess 3 is like.
you know this is another. I I think we've seen like a long tail of this like this rack where we enhance it downstream strategy just being like a little wonky and like
I don't know, causing some issues. So this is like another to add to that tally I guess so, anyway, I would just say, like, Yeah, got them like, would you be interested in working on this?
And also to the greater group like, Are we all okay? If I open an issue in
can trip to track it.
**goutham** 16:13 Yeah, I already just opened an issue in contract to track this.
And yeah, like, I, I'm going to use a custom sampler anyways, because I need to set per endpoint sampling rates because some endpoints are more useful and slower than the other ones, and tail sampling does like. It's just too expensive to do it correctly.
But like in the custom sampler that I have, I'm
going through the attributes and like having, like very brittle matching on the URL, or like the handler that is kind of being passed from rack if I can do it.
When I look at like my spans in the tracing ui, and I say, Okay, this span is not very useful, or this root span is not very useful. If I can use that information and have a standard config that is supported in the hotel collector. That would be amazing. But if not, I'm I'm going to have to maintain my own custom sampler, but like I would love to contribute the official jaeger sampling strategy.
but I don't know how to get around that whole rack thingy
**Kayla Reopelle** 17:24 Yeah.
Wonder if there's anything related to the like? Http. Semantic convention stabilization that could help us here? I guess the route is still part of the server span name. So
just thinking out loud that probably wouldn't help it could be.
I mean, it could be just a different issue. I wonder how different the span names end up being with regards to route
with the information we have available in rack. When a span starts versus what we get
from the other libraries that consume, or that, you know, depend on rack.
I think that would take some investigation. But I feel like.
I mean, I'm if you can
find an alternate approach to kind of get those names.
I I would be like welcome to reviewing that and seeing seeing if there's another strategy
we can, we can use
But yeah, that is, that is a tricky problem.
I wonder if other languages also
have encountered this, and if they have any solutions that we could leverage.
**goutham** 18:54 Yeah, sorry I was.
**Eric Mustin** 18:56 Hasn't.
**goutham** 18:57 Looking into. Go which is what I'm familiar with. And in go there is an option that you can set that this is not the final sampling decision.
So they kind of
rerun the span through sampling again once it's final, like, if you're changing this span name, I need to go and understand it. But they do mention that. Okay, if you're going to say that this is not the final sampling decision, then there's a penalty to it or something.
What I can do is I will put together a doc with all the information like, what information does rack have. I was sinatra or rails updating it? And how are one or 2 other languages doing it? And I can share the doc. And then we can see how we can tackle this.
**Kayla Reopelle** 19:46 That would be amazing. Thank you so much.
Yeah, let us know what we can do to help, or if you hit any roadblocks. But I yeah, thank you for taking this on and for doing all this research, it's it's great to have have another person contributing to the project.
**Eric Mustin** 20:03 Yeah.
yeah, I I hope there's a way where you don't have to contribute and maintain an entire new sampler to accomplish your task like your feature.
and it also feels like overkill in the sense that, like you're introducing. You know, the remote stuff is sort of like.
extra complexity onto like you're having to solve multiple problems just to get your specific, you know, issue out of the way. So
it would be like the only thing I can think is in your custom sampler. Can you import the sinatra or rails specific helper functions that are being used to infer the official name. And then, just.
you know, run the.
you know, basically read, you're basically duplicating the logic that sinatra or rails, or whatever are doing using what I hope are like
public Api, you know, public methods.
That was off top of my head. But I didn't dig into it.
but yeah, I? If if there is a creative way
where you feel like oh, you know, I could use second set of eyes on this, or like
you feel stuck and want some help, especially if you're not, you know, if you're coming from.
Go lang land and rails or ruby is a little scary or whatever just. You're not as used to navigating like. I think we're happy to help there, and like
that might be you know, I think, for all parties involved. Like we're, we've been very intentional within the ruby sig around trying to not trying to main, manage the surface area of everything owned in here, just because, like, as you can tell, like, it's a pretty small
group of folks who don't have a ton of dedicated time.
So if there's any way to avoid that. That being said like, if you want to contribute something like obviously like you're Prometheus Maintainer. You work for funnel like I think we'd be comfortable like with you owning. You know that so.
**goutham** 21:52 Again. If I'm gonna do this, it's going to be a separate gem that is out of scope of this repo. I think you know
it. It doesn't make sense. It's kind of like, yeah, I don't think it makes a lot of sense in that case. But I really want to make the Jaeger remote sampling strategy work. Because companies have built tooling around this. For example.
like at Grafana, we have tooling. That's like, okay.
**Eric Mustin** 22:16 Yeah.
**goutham** 22:17 Going to sample things down. But when there's an incident, we can say, Okay, this particular endpoint we want like higher sampling rate. And within 60 seconds.
**Eric Mustin** 22:26 Yeah, yeah.
**goutham** 22:26 So I really want
this tour, this to work. And I'm like, I'm getting used to Ruby. I'm writing more and more ruby nowadays. And this is a great way for me to also kind of get it. Dive into some of the details. Yeah, cool. Yeah. Let me put together that, Doc, and we can see what the next steps are from there.
**Eric Mustin** 22:44 Cool. Yeah, I think long term, I'm sure, like the OP. Amp. Folks have some aspirations to kind of solve some of the stuff, but in the short or medium term of like years I think something like a remote sample is probably the best
like supported strategy. If you want to contribute something official upstream.
awesome thanks. I have to. I have to. I do have to hop in like 5 or 10 min, but that was the only
think! That was the only one I had on here.
**Kayla Reopelle** 23:11 Okay, sounds good.
Nice. Alright. So
the next thing I wanted to chat about the configuration options that are proposed right now for the 0 code auto instrumentation. Pr, unfortunately, I had some computer problems and wasn't able to go to the config Sig this week.
but let's
I think it doesn't seem like there is stability among the different languages, for, like what configuration should be called, but my
like concern or curiosity was around like.
if these names line up with the new naming strategy that seems to get to to be
Oh, my goodness! I lost my train of thought new naming strategy for the file based configuration. I think that those configuration values are supposed to be able to be set by environment variables as well, and maybe have that transition. I'm I'm still not fully versed in it. But yeah. So I was just curious, like Sean, like when you were deciding the names for the configuration options like, did you have
any inspirations from other languages? Or you know, could you just yeah chat chat about some of your thinking with the naming.
**Xuan Cao** 24:44 Are you referring to all this environment? Variable name.
**Kayla Reopelle** 24:49 Yes, yeah. Yeah. Like, the.
**Xuan Cao** 24:51 Yeah. So most of them are like copy from the note. Jess, so they have this kind of a
specific particular name for the auto inspiration operators. I mean you. You can't use this
outside the operator because they're not.
They're not a part of their like standard SDK, they're just for their ultimate auto implementation and script
to make to make something easier to have a user to manipulate
mostly, just like user. What kind of a library they want, or they don't want, because otherwise they have to do like encoder configuration, which is not ideal for the alternation. So they wanted to have this kind of a
a variable. Oh, you want my variable?
Yeah.
**Kayla Reopelle** 25:48 Okay, okay, nice. And yeah, knowing that it's based on node,
is helpful, because at least then, you know, we're getting closer to a standard by having 2 different languages. If this is only usable with auto instrumentation.
do you? Does it make sense to add auto to the names? I know these names are already really long. So maybe that's not
helpful.
**Xuan Cao** 26:16 I'm I'm open to the name. I don't really have a preference on name as long as they work.
Oh, I know. Just by the way, I haven't checked the Priceline
audience audience position code. If they have this similar thing
because I think python is different, because, python. We have, like some kind of Bootstrap stuff that is
kind of it just doesn't need this kind of mechanism to decide what kind of library you want.
Whatever you don't so, but no addresses very similar to
to Ruby in terms of this kind of setting. So
yeah, again about naming. I don't have any preference. If you if you think auto and you can I will make the commit based on your course. Suggestion. Yeah.
**Kayla Reopelle** 27:08 Okay. Well, I guess I'll look a little more at what notice doing first, st I guess. Do we think there would be a benefit in, you know, not with this Pr, but maybe in the future, allowing more environment, variable configuration for
contrib and instrumentation.
**Xuan Cao** 27:30 You mean for this gem, or for just for general.
**Kayla Reopelle** 27:33 Just in general, for contriv like not as part of this pr, just part of a separate
future effort.
**Xuan Cao** 27:41 Don't know if if I can call for everybody, but for for myself,
less human variable, be better, because
one is to increase the like complexity, like something. And
but but anyway, for for myself, I prefer not to have too much variable. Yeah.
**Eric Mustin** 28:10 I thought the
the config like underscore config on scraps. I thought, that's just from Con. That's just something we have downstream like in contrib.
I didn't think that was operator specific.
**Xuan Cao** 28:24 This. You mean the our config opts.
**Kayla Reopelle** 28:28 Okay.
**Xuan Cao** 28:28 Yeah, yeah. So so all the yeah, this is not on the, this is pretty good for the operators, I think.
yeah, yeah, this is just try to replace the encode configuration. Yeah.
I think we have this in the opentime. Gio Page, to describe how this stuff works, and then how, when compared to the encode, encode, configuration, how things are related.
**Eric Mustin** 28:55 Right.
So just to be clear. The 1st hotel underscore Ruby enabled instrumentations that is, is.
that's operator specific, or is that? That's something we own.
Oh, let me check!
Thought I thought. I know I I wrote the second one hotel ruby instrumentation, you know.
interpolate in the instrumentation name, and then config ops. That's something
that we have. I don't know if there's a no, no, worries Catherine.
I was, gonna say, the only thing I have concerns about there with like
interoperability with the file based. One is that I know we don't support
like of the types of config options that we support.
I think Proc is not supported by this. Because that's weird and like has a I think there's some security implications for allowing people to just like write procs on it.
Bar. I don't know it was just scary enough where I was like, all right, like someone brought up, and we were like, All right, let's just not worry about it.
but that might be a like, I would say whether they have support for that, and then also the Ca, the precedence of like what comes for what gets over what overrides what is probably.
**Kayla Reopelle** 30:07 Yeah.
**Eric Mustin** 30:08 Worth clarifying. I don't think anyone cares about naming specifics too much. I don't know. Maybe someone has strong opinions.
**Kayla Reopelle** 30:16 Yeah.
okay, yeah. I guess my my concern with the names was just more like, if this was going to be auto instrumentation specific like, would we ever want to use this outside of that context like, could we imagine a world where?
you know, we'd want this name for something slightly different and couldn't couldn't use it. But I think.
yeah, if this, if this config Ops is already here, then this
**Eric Mustin** 30:54 Mantra enabled structure.
**Kayla Reopelle** 30:57 Is is good, and maybe
I guess we should probably just have a bigger conversation about configuration at some other point, anyway, and
decide how we want to handle the config file, and that will probably help us determine precedents and stuff like that.
**Eric Mustin** 31:16 Yeah, we have it where
I guess it's you configure it on an instrumentation by instrumentation and var basis. Like, so
the way that second option. Config ops. If you have, rather than being an array like, I think, the operator. One is the array instrumentations. Plural is
inc operator specific, but are under our equivalent in just our world is instrumentation.
then underscore the specific instrumentation, then underscore enabled. And it's just a Boolean.
It's in the bay, in the, in the.
of course, where everyone looks, the code comments of the base instrumentation.
There's some language that
was added there many moons ago.
So yeah, I don't know. I'm I'm thinking a lot. Obviously
**Kayla Reopelle** 32:10 Yeah, no, that's that's helpful.
okay, well, I guess I'll I'll make it to do myself to go look at and see how notice doing it, and maybe it makes, you know, just the most sense to kind of align with their structure.
**Eric Mustin** 32:22 Yeah.
**Kayla Reopelle** 32:24 And yeah, this this is helpful to to know like more about the scope with the environment variables.
**Eric Mustin** 32:31 Definitely unclear to me what you know.
If someone's just shipping all the Mbars, what actually like.
who gets who? Who's on 1st type thing.
**Kayla Reopelle** 32:40 Yep.
**Eric Mustin** 32:45 Sorry. That's a a
specific. You know what what the precedence is is what I meant to say.
**Kayla Reopelle** 32:51 Yeah.
**Eric Mustin** 32:52 Realize not everyone obscure understands my obscure advent. Castle references.
**Kayla Reopelle** 32:56 Yeah, it's all
Okay, cool. So I'll just say.
alrighty, okay.
**Xuan Cao** 33:12 Do you want to talk about this? Another one? I think you brought up in the comments about long list of
mapping for.
**Kayla Reopelle** 33:19 Oh yes!
**Xuan Cao** 33:20 That's another kind of I think this relate to the what is the enable or the you asked about.
Do we need to maintain that list. I have some feedback. Again. This. This is borrow from Nodejs, because there is very similar from node and ruby.
We can like python to Bootstrap stuff, and then
to decide what library to you to enable or not enable. And yeah, I don't. A ruby. Oh, sorry not use the hard code. I don't know how they maintain their stuff.
Maybe you just manually update, but I don't like it as well. But at that point I don't have any like good solution. But anyway.
It really depends on. If if user prefer.
like, I think it's more like user education to tell them what to do. But that, anyway. Yeah.
**Kayla Reopelle** 34:21 Okay.
yeah. Alright. Well, I'll I'll get more familiar with what's going on with note there and and respond.
but yeah, I guess if we
you know this, I think we can still merge this. Pr, it's been open for a really long time.
but
yeah, to to make it easier just to reduce us, forgetting if we do need to list all of the instrumentation on there.
Maybe we can work on that later.
Okay, the other
thing that I wanted to point out. So there's this new hotel bot that has been creating Prs and is replacing the open telemetry bot
but it has like
slightly different structure. It has an action that you run to kind of create a token, and then you call that token elsewhere.
We have had problems in the past with trying to use the open telemetry bot token for
for releases. And the the problem with our release setup right now is that since we're using the Github Token, that token doesn't have permission to run the Ci on Prs that it creates. Supposedly this hotel bot does so. This pr, is just an attempt to integrate this new system and see if that helps resolve. The problem of needing to push empty commits every time we open a release. Pr.
and what else? There's also this net Http test failure that's been persistent. I don't think it's necessarily
related to anything that we changed. So I
I don't know. I've I've looked into it a little bit. I'm not really sure what's going on the resources online seem to point to like, maybe something changing in Github actions about like
the amount of resources we have there.
But yeah, if anyone has time to look at this. That would be great. If not I might just open a Pr soon to skip these tests.
Until we can spend a little more time to figure out what's going on. But for now, just
so, everyone's aware, I'm kind of merging Prs, even though this is failing.
Oh, yeah, and I broke the Ci for the Http client, simcom Pr.
Where is that?
So? I made a mistake and accidentally closed the Pr. Instead of merging it. I don't know what I was thinking, but for whatever reason that has stopped up
the commit message checking system because it's looking for.
I think a merge that doesn't exist yet. And
so, since this is a required
a required action in order for a Pr. To pass Hannah, I wonder if
you could like open a new pr for the same
stuff, and maybe we'll just link this one. I feel like that's probably the best way to get out of this, though if anyone has other ideas like open to that as well.
**Hannah Ramadan** 38:19 No, I can. I can do that probably pretty easily, so
we'll just close this one and then open a new one and say, oops, so.
**Kayla Reopelle** 38:27 Yeah, I think so. I'm I'm gonna hit update branch. I don't know if I've tried merging main into it again yet.
Let's see, usually this runs pretty quickly.
But yeah, if not, then I think exactly. Yeah, exactly. That process.
Oh, yeah. Oh, passed. Okay. So it just needed a merge domain. Alright.
**Hannah Ramadan** 38:50 Interesting. Okay. Cool. Well.
**Kayla Reopelle** 38:52 Learned learn something new. Okay? Well, false alarm.
**Hannah Ramadan** 38:58 That stuff always seems sensitive.
**Kayla Reopelle** 39:00 Yeah.
Yeah. And they've changed the
permissions now around, admin like you can get admin access to override these things. But it's a little more complex.
This is the last thing I had on our list.
this Graphql data loader is not compatible with open telemetry tracing.
It's an old issue that has had some more activity recently.
It was. Yeah. It was closed and then kind of reopened in April.
I don't know if this is anything that like, I think.
our most old is pretty good at
handling the Graphql stuff and maintaining it.
But
I guess if anyone had been running into this or have any insights here, I thought I would just call it out if
if someone wanted a training.
and the next step is just to tag him again to see if
he's willing to hop back in
alright. That was our agenda. It's a little more full than we've had the past couple of weeks. Is there anything else that people want to discuss.
**Xuan Cao** 40:53 Oh, I have one something about the log from the country. I think you've opened that for a long time, and then
I just wanna like, see? Like, why, why are we gonna have that.
**Kayla Reopelle** 41:08 Which one close.
**Xuan Cao** 41:09 Yeah, yeah, that's right.
**Kayla Reopelle** 41:13 I think we just need an approval. I I don't.
**Xuan Cao** 41:16 Oh, okay.
**Kayla Reopelle** 41:16 I know Ariel had some concerns about like
about patching the ruby logger. I don't have those concerns, but I'm open to other strategies. If if people do, I guess we patch the ruby logger and new relic, and and have been doing that for a few years now, and haven't run into any problems.
I guess I'm seeing the Pr. Is failing right now, so I should probably take a look at that to get it working again. I'm not sure what is going on here. Oh, it looks like rubocop failed so I can get that fixed.
But yeah, I think I would love to get this out there and kind of wrap it up.
Maybe the last concern would be about naming
it seems like naming is my favorite topic these days. With
the name right now, like open telemetry calls logs,
like log adapters, bridges instead of instrumentation. So there was a question about whether we needed to.
you know, put this outside of instrumentation and make it in a separate category called bridges.
So yeah, I guess, rubocop.
Any concerns about
patching the logger, and then where exactly we put this gem and what it should be called. Those are the 3 things that I think, are blocking it.
But, Shawn, if you think this is ready to go I'd love your approval on it, and can do like a final call in the slack and
see if anyone else wants to approve it. But if not, then I think we can merge
with a single approval. We've done that before.
**Xuan Cao** 43:17 yeah, yeah, I think I think it's great to have like, like all of the instrumentation. And like you said, like adapter similar to our resource detector.
**Kayla Reopelle** 43:27 Yes.
**Xuan Cao** 43:28 Thinking about have concern about the patching the logger. So if we outside the implementation, then user can decide. If we want to try this out or not.
you can set a like solution that then they have the installers, because it's part of a like all, I guess.
Yeah. And then.
is it any also easier for them to like disable or not disable? Just simply just using or not using it? So.
**Kayla Reopelle** 43:57 Okay.
Hmm.
Was there anything else I missed here that
or do? Do you think that covers your concern?
**Xuan Cao** 44:12 Oh, no, I think it's like, I just cover everything. Yeah.
**Kayla Reopelle** 44:14 Okay, sounds good.
Cool. Then I will do this week.
Nice. Anything else that we want to chat about?
Oh, and
with the fix in core. I think I was just going off of trying to match whatever the words were in the spec. But you can ignore those we don't. We don't need to change the names. So I think that that's
**Xuan Cao** 45:09 Oh, already already changed! It.
**Kayla Reopelle** 45:10 Oh, you did. Okay.
**Xuan Cao** 45:11 Yeah, because I checked. I think the minimum is more casual and then more like academia saying so.
**Kayla Reopelle** 45:20 Yeah, that's a good point.
Okay, thank you.
**Xuan Cao** 45:27 The only thing I have to complain is, why Github doesn't have like commit all suggestion. Yeah, I have to like click one. If if I, if I do like, commit a suggestion, I had to do one by one.
**Kayla Reopelle** 45:39 Oh, really, you can't do like a batch.
**Xuan Cao** 45:41 I don't know. You can.
**Kayla Reopelle** 45:44 Yeah, when I've seen it.
trying to think of like a Pr.
let me. Just. I'm sure I have some Pr up here that we can play around with So
so when I submit these, I see this add suggestion to batch option.
**Xuan Cao** 46:28 Oh, okay.
**Kayla Reopelle** 46:28 You can click on those, and it'll just put all the suggestions in one, and you can commit them.
**Xuan Cao** 46:34 Oh, okay, I haven't see this this page, but the always just looking at the the code tag. And then.
**Kayla Reopelle** 46:43 Oh!
**Xuan Cao** 46:43 Options to like? Do the other.
**Kayla Reopelle** 46:46 Got it. Okay?
And I I've always looked at it from the files changed. So that that makes sense. I'm surprised that it isn't on
it. Looks like it might be here, too, but
**Xuan Cao** 46:59 Yeah, I'll I'll I'll pay more attention. That's fine.
**Kayla Reopelle** 47:03 No worries. Yeah. Thank you for asking.
Cool.
Alright. Last call anything else we want to discuss
cool, alright, nice meeting today, everyone. We had some good discussions. And
yeah, we'll see. See you all next week.
**Xuan Cao** 47:34 Okay. Thank you. Bye.
**Kayla Reopelle** 47:36 Bye.
**Hannah Ramadan** 47:36 Thank you.
