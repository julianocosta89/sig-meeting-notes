SIG: Ruby SIG
Date: 2026-07-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 01:39 Hey, Xuan!
**Xuan** 01:42 Hello. Hi.
**Kayla Reopelle** 01:48 Don't know if Matt's joining us today. I know Hannah won't be here.
So… Yeah, let's wait one more minute, and then we'll get started.
**Xuan** 01:59 Okay.
**Kayla Reopelle** 02:36 Good morning.
**Matt Wear** 02:39 Good morning.
**Kayla Reopelle** 02:58 I think this is everyone today.
The Spec SIG… Today, I only caught a middle part of it that was about Basel support, and… issues.
Matt, was there anything that you noticed that, you wanted to call out for this meeting?
**Matt Wear** 03:37 I don't think there was anything all that relevant for us.
To be honest.
There was this remove attribute ordering from the spec compliant Matrix, and that's basically… there was… A row in the matrix that said that, like, attribute insertion needed to retain order, but… It's nowhere in the specification, so they were just removing it.
**Kayla Reopelle** 04:08 Okay.
It's like we… Supposedly… did this?
**Matt Wear** 04:17 Yeah, yeah, I think we're… We were compliant, so it doesn't really matter, but…
**Kayla Reopelle** 04:26 Okay, nice.
Yeah, I had one core issue, maybe more than one. Oh, and Bart is here, which is great.
That I wanted to look at, and I believe this is a link to your issue, Bart. So, I don't know if you want to present it, not to just, like, have you walk in and put you on the spot.
Go ahead.
**Bart de Water** 04:54 It's happening, but that's okay.
**Kayla Reopelle** 04:55 You can always say no, you don't have to oblige.
**Bart de Water** 05:00 No, I mean, long story short is, I… in order to aid some of our, sort of, like, investigations in bad actors, I wanted to add Cloudflare geolocation headers, that they were already sending, but that we were not surfacing in our, hotel.
And while I was testing with my own IP address to see if everything showed up correctly, I apparently am now located in encoding error instead of Montreal.
And then I was like, okay, this is the end of the day. I pointed my agent at it, and like, go figure out, like, is this a, you know, is this our vendor problem? Is this, like, somewhere in Ruby? Like, where is this happening? And I pretty quickly pointed out that this was happening on the Ruby side of things, so also within our purview to fix.
This is probably not a complete fix yet. This was very much of, like, here's the factories, go and figure out where this might even be going wrong, but, yeah, one way or the other, it seems that, where that ASCII 8-bit strings coming from RAC, break when they are, sent over OTLP, where UTF-8 is expected.
I think Thompson Tomo, I'm not sure what his real name is, is correct that we need to make this fix in a bunch more places.
But I was curious if, like, directionally speaking, Yeah, like… Is this something that, you know, like, I saw that there's, like, a UTF-8 sort of, like, encoding helper function? I forgot the name of it.
If that one is the right thing to use here, and whether or not, you know, like, we should have a last line of defense before we start exporting the data, or if this is more a thing of, like, no, the instrumentation libraries are responsible for creating UTF-8 strings, and therefore it should be fixed on the rack side, and not on the, sort of, like, last bit before exporting side.
**Kayla Reopelle** 07:01 Nice.
Yeah, that is also my question, and I feel like I don't have a clear… answer, I… didn't look too closely, because it was also end of my day when I saw your post, but I'm curious if we're doing any conversion in the exporters right now anywhere else, or if our exporters are just assuming that everything that they receive… is correctly encoded. Because we do have that helper, but the UTF-8 encoding helper really only is being called right now in the database instrumentation libraries, and that kind of surprised me, because I feel like we'd want to check UTF-8 encoding in a lot of other places, too.
So then, yeah, I feel like it's kind of a decision, too, about… code sprawl? Like, do we need to have something… you know, maybe in the SDK that's checking UTF-8, or is UTF-8 not always a requirement? Those are spec questions that I have.
And… there was something else in there, too.
Yeah, or is having, like, it in more than one place a good idea, just in case one fails? I feel like performance is another thing that could help us make the decision. Like, I don't know if taking care of it once in the exporter is maybe easier than… Checking it in a bunch of different places, you know, in the hot path.
I'm curious… yeah, mostly I have questions right now and not opinions. Matt or Xuan, do either of you have opinions on this?
**Xuan** 08:52 I'm just, I'm probably just gonna, To check other languages, if they have the similar… encoding issues, especially JavaScript and Python. So, I think I will… I can… I can look at this here after I… Check out the languages.
Yeah. I mean, if this is, like, the common issue, then, It will be your first one to fix this, and maybe we can… broadcast this issue to everyone. But, yeah, I would, look at other language person.
But I think it's a… it makes sense to, encoding to ensure the… All character is, safe, too.
In critical, so… Yeah.
**Bart de Water** 09:40 Yeah, my hunch is also the SDK, because otherwise you're going to be sprinkling this same fix throughout potentially every instrumentation library.
I, I did sort of, like, let an agent take another run this morning on, like, okay, you know, like, what would a proper fix like across, like, you know, all the signals?
And it did come up with, extending the UTF-8 encode helper to handle specifically ASCII 8-bit, strings, then try to convert them to UTF-8.
and check if the encoding is still valid. If so, return the converted UTF-8 string. If not, raise like before. That would fix the Montreal case, because that was sort of, like, a pretty obvious one, but still… Make sure that you're not just throwing any kind of, like.
sort of, like, binary data that's coming through as a Ruby string, trying to submit that over the wire.
So I can push over that new branch, because I think, you know, from what I'm sort of, like, sensing here in this discussion, that seems like a direction that would not at least be rejected out of band completely, and that would be a more complete, suggested fix than what I have right now here on GitHub.
**Kayla Reopelle** 11:04 Yeah. I think one other thing I want to understand, too, from the spec is, like, are there any cases where… we should allow things that aren't encoded in UTF-8.
You know, are there other exporters? Like, does… I guess since it's a protobuf encoding error, that kind of takes out HTTP and gRPC, we, with Ruby, don't have, like, a file exporter or a JSON exporter.
But… yeah, I'd be curious if the spec… Has any encoding requirements that we need to adhere to.
**Bart de Water** 11:46 Don't know either, but I can try and figure it out.
I would imagine that there is a distinction on the wire protocol between a string and, like, real binary.
**Kayla Reopelle** 11:56 Yeah.
**Bart de Water** 11:57 But, that is definitely a guess on my end right now.
**Kayla Reopelle** 12:16 Okay, well, Xuan, I'll be curious to hear what you see from the other languages.
hear, see, read. And… Yeah, and we'll keep looking… at the spec, and thinking about where this fix goes. Are you comfortable if this takes, you know, another cycle or two, Bart?
**Bart de Water** 12:39 Oh yeah, like, I mean, I can always run a fork in the meantime, right?
**Kayla Reopelle** 12:43 Sounds good.
**Bart de Water** 12:44 It's, no, it's, like, not super urgent to fix, but it does seem like, It should be fixed.
**Kayla Reopelle** 12:50 Yes, yeah, I agree.
Yeah, this seems like a use case that people could be running into and just not realizing it right now.
**Bart de Water** 12:59 Yeah.
**Kayla Reopelle** 13:03 Okay, cool. I'll… I wrote down some notes, I'll add those after the meeting.
Let's see, there's one other issue in here that I meant to add to the agenda.
That I just wanted to put on people's radars. This, like, total recorded attributes when log record attributes is called.
There is an issue where currently because of Ruby magic, and also how the spec has changed since the logs were first, implemented, you can just instantiate a log record object directly and mutate its attributes before you actually Call on a mitt on it.
And because of that, the current expectations were only log records will only be created when OnEmit is called.
that causes the total recorded attributes number to be inaccurate. And so… we've had some discussion on, you know, how much this fix should cover, like, does it need to look more broadly at how to fix attributes? I think right now the decision is to keep it pretty narrow and only look at making sure total recorded attributes is actually measuring the correct thing. Which, after diving more deeply into the spec, it should only It should be recording all of the attributes that were seen, but in such a way that when you… compare it with the final attribute size, it only represents the difference of attributes that were dropped due to limits.
So, I think there's still a little more back and forth on here, Thompson Tomo, James, reached out to the spec channel to make sure that we're doing this correctly.
But, we'll probably have more on it soon. Just more of a heads up. I think… I think we're… we're good here, but just to let you guys know.
Is there anything else in core… That we want to look at together today.
Let's see, there's a release… API, SDK, Metrics SDK… We're getting the attribute support to instrumentation scope for tracers… I… Don't know why this is showing up here, so I'll have to take a look at that.
Okay, anything else in the pull request encore that we want to look at?
Okay, looking at issues… we don't have any new issues as of this week.
That brings us to Contrib.
I guess before we just go through all these, is there anything else that people specifically want to talk about today or look at together?
Alright, Matt, I know I still owe you a review on the TracePoint PR that you presented to us last week.
Yeah, we'll just click through the rest of the links then. I think if anything pops up, we can talk about it, but, the meeting will probably be pretty short.
We have… A documentation update for active support, from a new contributor.
Bunch of renovate stuff… Oh, there was one issue I did want to talk about. So this was a discussion I feel like we have, kind of.
Maybe, like, once a year.
Basically, in this problem, it seems like there are a lot of spans that are just a single semicolon in this Postgres instrumentation because of the way that active record… Does, its active checks on the database connection, and in order to do that, it just makes a query with only a semicolon.
Trilogy ping spans had a similar issue. That's also how Active Support, checks to see whether Trilogy connections are active. But, So we were able to confirm from the reporter of the bug that it does seem like it's these active record connection, issues that are coming up.
But, we… I'm not quite sure what the best solution for this would be.
One, the idea that they had was to make a span for the active check, so that you could see from active record, like, what is actually causing this ping, and that would then also… solve an issue for Trilogy, and I think other database, adapters, or not adapters, but database gems.
There was a discussion on this issue back in the day. Okay, maybe not the issue, maybe the pull request.
That there was some concern about… adding a configuration option to control whether or not the ping spans got recorded, just because… you know, this… there was some question about, like, is this the right scope? Is this the right place for this to happen? And I think the conclusion was… that… Somewhere in here. Yeah, using custom samplers instead to pull out those particular like, ping spans.
Yeah, so the semicolon query coming up again here, too.
So yeah, so I guess I'm just curious about what… we want our best practice to be in this situation. Do we recommend that people… use custom samplers, do we update active record instrumentation? That would create a ton of spans, which might be a huge increase in… in data that people aren't quite ready for or are interested in, it's not something that we'd have an active support So, like, notification for, so we'd have to do some monkey patching on that specifically.
Yeah, yeah, so mostly I'm just looking for ideas and, Suggestions on how to best solve this issue that kind of keeps coming up.
**Xuan** 20:34 I actually prefer to use, custom… -Oh.
Collector, or processor, not to touch.
Over on.
implementation, because that will increase a lot of burden on us, and a lot of work for us. And It will… Also, kind of create a, additional, traffic, traffic options.
**Kayla Reopelle** 21:00 Yeah.
**Xuan** 21:01 So user TPUs have a… A lot of, customer guys, requests, the… they can do it on their own processors. And actually, I think some people, well, they want some, some kind of a… URL.
they also do it in their, custom processor, so it ignores this kind of a thing, so I would say, yes, we should ask the user to do it in their, custom processor, yeah.
**Kayla Reopelle** 21:33 Sounds good.
Any other thoughts or opinions on it?
**Bart de Water** 21:46 Feels like this is the same kind of, like, shape.
Where we've configured our rack instrumentation to ignore the slash up path, which is like the Rails default health check endpoint.
Because that just otherwise also just creates, like, a ton of useless spans that we're just not really interested in.
I don't know if it makes sense, though, at the database level to, say, ignore queries that exactly match a single semicolon.
**Kayla Reopelle** 22:17 Yeah, right. And is that overhead in a weird spot, too? If it's, like, checking inside of your database query as it's happening?
**Bart de Water** 22:29 Not sure if it would be too bad, because it should hopefully be a simple string comparison, but…
**Kayla Reopelle** 22:34 Yeah, if it's only an identical one and you're not including, like, query parameters or anything like that.
**Bart de Water** 22:40 Exactly.
**Kayla Reopelle** 22:40 Yeah.
Yeah. Also, I just noticed there were a bunch of things in the chat that I did not see earlier.
Was this… okay, this was mostly related to the encoding discussion, from earlier.
Take a look at this later.
**Bart de Water** 23:05 I think, Matt, I think that one actually… is exactly what I was looking for. It says that strings which are valid UTF-8 sequences should be converted to any value string value field.
And in this case, Montreal, even if it's coming in as ASCII 8-bit, it is a valid UTF-8 sequence, so I think it's fair that we add a special case there to the UTF-8 encode function to handle that.
and convert it to a UTF-8 string, if it is a valid UTF-8 string.
Thank you.
**Kayla Reopelle** 23:50 Okay, alright, well, I think then that's contribib, unless there's anything else people want to talk about there.
Auto instrumentation, We're still working on getting the first release out. There's a new issue in the community repo.
To try to look at different permissions for GitHub token, to see if that's what's blocking us.
But hopefully, we'll have a release very soon.
And yeah, we have our release PR.
Attempt issues.
Alright, well, I think that's about it then, unless anyone else wants to discuss.
Anything?
Okay?
I'll take that as a no. Alright, I will see you all next week.
**Xuan** 24:57 Thank you.
