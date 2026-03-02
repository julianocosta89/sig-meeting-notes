SIG: .NET SIG
Date: 2025-06-24
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Julius Koval** 00:50 Hi.
**Martin Costello** 00:54 Alright!
**Alan West** 02:08 Hey, folks.
we're good. Thanks for getting the agenda started.
Yeah, go ahead and put your name in there, and
good looks like we got a few things, Martin.
if you wanna take it away.
**Martin Costello** 03:05 Yeah. So I 1st one. Well, there's 2. Ef core related ones.
The 1st one is mainly just a nudge to get a review on, because I know I've done a bunch of Prs recently, but this one's like not just
fixing tests and stuff. There was a Pr for an issue back in November, whereas if you, if you're using sequel client, and ef together in the same app.
they don't interact correctly together, and the the spans don't get attributed properly. Someone did a Pr to do that, but then it got reviewed, and it's just great, but needs tests. And then they never came back to, and it got auto closed. So I went and dug it up and picked it back up, and I did the test, so we don't have to review it right now.
But it was just that a prompt to get a look at that while I was at it as well, today I also discovered there was a bug, and that was already there, that I think the lack of
the Sq. Light coverage had.
which was in some circumstances, the Ef core tracing, I think tracing is the right word infrastructure.
The dB context isn't always there, and the code assumes that it is
so the most recent 2 commits I put in today that I haven't put in the change log yet.
Address that, and then I've done a Pr. Off to ef call to fix that, but I imagine that's the sort of thing that will only be kept in Donnet 10 if it gets accepted.
**Alan West** 04:48 Okay, yeah, fantastic.
I will take a look at this. And see if we can get this. This merged. This will be this will be good.
**Martin Costello** 05:01 There might be. There might also be some overlap with the change you did recently related to the sequel tests.
I know you did. A big change related to that. So I don't know if some of the stuff I've done might be need reworking, based on that.
**Alan West** 05:21 Okay, yeah. I'll look at it with an eye for that, you know. To be honest with you, I've not
I've not spent a lot of time with the Ef core instrumentation. So I see your next
step is your next. Your next topic is to take ownership, which I think is also great.
yeah. And I mean whatever testing you've done here, I it's kind of long, so I'll I'll take a look through this. But if
whatever whatever tests you have here, I think will be good. And then, you know, if we want to like, follow up and and converge kind of a pattern between the 2. Is that kind of what you're saying.
**Martin Costello** 06:05 Yeah, yeah.
I started off by copying what was there about 2 weeks ago, and then turned it into what's there now and then. But then, since I copied that code, you did a bunch of big changes. So it's kind of diverged from what's now there, even though it was similar to what was there.
**Alan West** 06:24 Okay, okay,
yeah. I would say, like, I mean, I guess I can review this Pr as is, and you know, just get it, get it in place, if that's your preference, and then if you, if again in, follow ups
and merge.
**Martin Costello** 06:42 I I'm happy to. Well, yeah, I
I am willing to do like Post fix up Prs. If you wanna like. Converge what I've done to something else to like. Get the ball rolling, but I'm happy to do it in place, if that would be preferred.
**Alan West** 07:00 Yeah, I guess it's up to you. I mean, what? What would you do? You have a preference.
**Martin Costello** 07:04 So
if if it was, if it was entirely up to me, I'd rather get it merged and moving, because then that fixes the functionality, and then the test rework is then just refactoring.
**Alan West** 07:17 Yeah, let's do that. Then I'll try to get this merge or or reviewed merged.
today, assuming whatever I don't have any
huge feedback or changes that are that I think are needed.
And then, yeah, we can carry carry on like that.
That sounds good.
**Martin Costello** 07:38 Sure that works for me. Thanks.
**Alan West** 07:44 And then, yeah. So the so the code ownership, I think.
sorry. I think this was out. You've had this out here for a while. I've just been meaning to basically approve it. In fact.
it's good to go right.
I'll just merge.
**Martin Costello** 08:03 It, it should, it should be. Yeah, yeah, I just thought I just thought I'd
prompt on it as it had the the relevant reviews as I was talking about ef core, anyway.
because because yeah, like Matt, he's a colleague of mine. He's like been working on a Pr to add
metrics to the provider that isn't finished yet. And then I was digging around in the issues and looking bits and stuff. And then we just noticed no one owned it. So between us, we're happy to sort of pick up trying to look after it.
**Alan West** 08:36 Perfect.
Yeah. And at some point
I I've been. I've been a little bit strapped with time, but I am looking to
finalize the SQL. Client work which I think we should be able to drive to stable soon.
I
I will be interested in in thoughts about what to do with entity entity framework. It's it's a little bit
There's some things to think through there in the sense that it'd be great if
we could find a path to stabilizing it. But the thing that makes it a little stickier than something like SQL. Client is that there are
entity framework supports certain data stores that
don't yet have stable conventions. So
you know, maybe maybe some thoughts around how
maybe if we could drive it towards stability, that it's like for any
for any data stores that aren't yet stable.
Maybe those are like opt in or somehow configured. You have to like explicitly configure them on. I don't know. Those are the fuzzy thoughts that I've had
But things for you to to chew on, I suppose.
**Martin Costello** 09:58 Yeah. Okay, thanks for the background. I'll have a think about that in the background processing.
**Alan West** 10:07 Sounds good.
That's merged. That's official.
**Martin Costello** 10:12 Thank you. And then final thing for me was just as we've had a bit of a dialogue in the Pr itself.
Yeah, about that test that keeps failing. I'm not sure how to proceed with that one, because it the.net framework variant of the test where I've made the edit definitively fails on my computer.
It like just doesn't does not pass. But it works. It works for you. Apparently it works in Ci. So I was just wondering if any suggestions on angles for further investigation, because to be to be selfish, it's really annoying for me that I have to keep.
**Alan West** 10:52 Yeah.
**Martin Costello** 10:53 Local edit to get the test pass. But at the same time, if it's something really strange
to do with my computer, then I'd like to investigate it and fix it. But if the genuine is a bug, then there must be a problem with the Ci setup in some way that it isn't immediately obvious from that.
**Alan West** 11:18 You know, I think I actually have the
yeah, I got the project open right now.
Maybe we just try this real time just to confirm that that
you know I'm I am run, in fact, running the test in the same way as as you are.
**Martin Costello** 11:38 You've got visual studio open and you're running them there because I can see that you've got the green text there. So it looks like, you're doing what I'm doing.
Which is yeah for for me. They like definitely fail on the command line and the visual studio. But I just.
Oh, okay.
**Alan West** 11:54 You know what I lied, you know.
**Martin Costello** 11:57 But.
**Alan West** 11:58 Because this is the integration test right?
**Martin Costello** 12:00 Yes.
**Alan West** 12:01 Yeah, no. Because Docker needs to be running. So.
**Martin Costello** 12:06 Cause. I only I only suggested that in the comment today, because I did exactly this this morning because I thought maybe this something has changed in Maine.
and maybe it's fixed itself. And then the test wasn't failing. So maybe it has. And then waiting for a deeper dive. And it's like. Oh, no, it's skipping, because Docker is not running. Then I've fired Docker up, and then it failed.
**Alan West** 12:30 well, I can try that offline. Yeah, you know what? That that may be. Problem. I was just kind of blindly running the test and being like I don't see anything.
**Martin Costello** 12:41 it's it's possible as well, if that's what it is. It might be a fluke that I found the problem, because, recent these recently in parallel to doing open work. I've been doing some other Grafana stuff where I've needed. Docker turned on so it's probably been on, but not intentionally.
and then I've like pivoted and done something hotel, and then it's ran the test that wouldn't normally run. And then it failed.
**Alan West** 13:11 Hmm.
yeah. The other thing I'm looking at here is
just trying to refresh my memory. What exactly this test case that you've excluded
is that it's the 3rd parameter is false.
**Martin Costello** 13:36 So the the difference appears to be that on.net framework it's not capturing the command text, but it does on.net modern.
So what I've done is I've just hashed. Find what the expected result of the test is, and that, like near the front of the test, it's got like a hash to find, says, Oh, if it's net framework, then don't do this
so it could be that it's there's actually a bug somewhere, and it's flushing out, and what I shouldn't be changing the input. But I don't have enough of a background
on this yet as to what the right answer should be so I've assumed it's a behavioral difference between the 2.
That's intention.
**Alan West** 14:20 This is actually.
yeah, I think in.net framework for stored procedures.
I actually suspect this. The behavior is that it will not include the text.
is that what you're saying you're observing is in.net framework, based.
**Martin Costello** 14:51 See ya.
**Alan West** 14:51 The command. The the text is not Sp. Who.
**Martin Costello** 14:55 Yeah on. It's just null on it framework. And I've assumed that's an intentional behavioral difference. So that's why I've got the conditional test. Input. But if it turns out that's not intentional, then it's just a bug, and I need to. And then I need to dig into why it's not there.
**Alan West** 15:11 I think now that I'm looking at this little more closely. If my memory serves me, I I will. I'll look at. I'll look offline at this more closely. I actually do think that this is.
I won't necessarily call it the intended behavior. I think it is the current behavior, and whether it's the correct behavior is actually
a question that needs to be answered.
**Martin Costello** 15:37 Okay.
**Alan West** 15:40 I think.
Assuming it's the it's the current behavior. Then I think what you have here is probably fine, and we can get, you know.
we can get you going, since I understand the annoyance. And anyways, this is part of
what I need to address. As I'm wrapping up this instrumentation, so
I can circle back and figure out what the what the correct answer is for this.
**Martin Costello** 16:09 Okay. Great. That works for me. Thanks, Alan.
**Alan West** 16:11 Okay?
cool.
And Hello, Julius. Yeah. Event. Name.
**Julius Koval** 16:29 Yeah. So I guess I was just wondering if,
if there's any update on this, because we
I know we were discussing it last time.
and I guess the conclusion was that we haven't really decided on anything.
**Alan West** 16:47 I? Yeah, I'm sorry about that. I had a
an unexpected short week last week, so I didn't totally close the loop on
some of the thoughts that I had with this, though I think we had a pretty good discussion last time.
And I know that there's been a little bit of discussion on the issue. In the
in the meantime, I'm I'm warming up to the idea that we
basically just carry forward with your Pr,
They're
let me ask this to to Blanche.
Would you say that kind of where you're leaning in your comments here? And I know Mothra was here last time. Kind of
seconding your your comments? Would you say that Julius's Pr is basically
in the spirit of what you're suggesting? Basically like.
run with event, just mapping iloggers event, name to event. Name in. For now and then.
if we see a need, we can
add something like this later. I believe that's essentially your take.
**Mike "Blanch" Blanchard** 18:19 Yeah, that sounds reasonable to me.
because we don't really know what people are doing with it. So
that gives us the ability to like, get feedback
before we go and ship some Api. We might later regret.
**Alan West** 18:41 Think that's fair.
So, Julius, yeah. I
again apologies for the the the slowness of this review. But I think again, I think I'm kind of warming up to it. I'm going to give it a another pass. Just kind of looking looking at your Pr.
One last time, and I think I'm I'm feeling good with going forward with it.
**Julius Koval** 19:06 Okay. Cool.
**Mike "Blanch" Blanchard** 19:12 And just to know, you know, if anyone
is disrupted by this change for some reason I don't know why they would be. You can always drop in a processor to do whatever modification you want.
**Alan West** 19:37 Yeah.
The way you'd the way that that would have to work is you'd basically have to like, totally
replace the event. Id right on the log record.
You could do that in a processor.
**Mike "Blanch" Blanchard** 19:58 Yep.
**Alan West** 20:00 With whatever you want.
**Mike "Blanch" Blanchard** 20:05 You could combine the Id and the name, or you could swap in some
totally different value from somewhere. It's
there's really no restriction there on that Api. It's just event. Id has a public setter.
**Alan West** 20:28 yeah.
okay.
I think that's reasonable.
So.
**Julius Koval** 20:49 I think that's.
**Alan West** 20:52 Sorry, Julius, were you going to say something.
**Julius Koval** 20:54 Yeah, just one more thing, which is, I guess, unrelated. But he mentioned that Raj is coming back from the holiday. I'm not sure when.
**Alan West** 21:07 I actually don't know when Raj is coming.
Pack.
Do you happen to know Blanche.
**Harsimar Kaur (Simar)** 21:15 He's set to come back end of July, I think 31.st
**Alan West** 21:23 Okay. And end of July. Okay, so another month.
**Harsimar Kaur (Simar)** 21:25 Yeah.
**Alan West** 21:26 Oh, are you on his team.
**Harsimar Kaur (Simar)** 21:28 Yeah, I am.
I'm just here to listen in learning things.
**Alan West** 21:32 Oh, right on right on
Yeah. Welcome
good to know. Yeah. I I thought it was. I thought it was sometime in July, but good to know the end of July.
Forgotten the exact timeframe.
Julius. Where is there a particular reason? You were asking about Raj's.
**Julius Koval** 21:59 Well, I think
I think Mike was talking about some plans that he had for the bridge. Api. If I recall correctly.
**Alan West** 22:14 Oh, are you referring to the discussion of implementing the bridge Api effectively, with like on top of ilogger.
**Julius Koval** 22:25 Oh, yeah, I think so.
**Alan West** 22:31 Yeah. Raj had done some like Poc work on that a while back.
though I don't know exactly what the the state of his thinking was. So yeah.
**Julius Koval** 22:48 Yes, I was just curious about that.
**Alan West** 22:54 Yeah, we can. We can. We can poke him with that. And when he's back
I'm equally curious, like, kind of, I would like, I would like to see that that move forward in some way or another. So.
but that has a that is a thing that I think will be good to have Raj back here.
or.
**Mike "Blanch" Blanchard** 23:22 It shouldn't be a blocker for the Pr. Though. Right? Cause it's it's just going in as an experimental thing.
**Julius Koval** 23:33 Of the locker.
**Alan West** 23:33 Hpr. The event name.
**Mike "Blanch" Blanchard** 23:36 Yeah.
**Alan West** 23:39 No, I don't think so. I I see these
as yeah, because it's because it's experimental. I don't see a big issue with that.
**Julius Koval** 23:51 Yeah. I was just wondering about the status of the
one of the bridge Api whether it's gonna get whether it's gonna get
stable, I guess, in the near future.
So that's why I was asking.
**Alan West** 24:09 Yeah.
yeah, we we should wait for Raj to get back.
I can't comment necessarily on a on a particular timeline offhand.
I would want to better understand kind of Raj's thoughts around
the ilogger approach that he had experimented with, and
from there we can probably more concretely talk about timeline and exactly what we're gonna do.
Okay, maybe we can take a quick look through.
Where was I looking at?
Let's look@prsfirstst
I think there was just one that I was kind of interested in talking about. This is a confusing one. This is just some
analysis stuff.
I haven't looked at this one yet, but this has been a long running one.
wanted to open up this one
to get some thoughts from folks here on this call, maybe, namely, you Blanche.
I was studying this before the call a little bit to get my head around what they're trying to achieve here.
A while back.
Steve commented on an issue here. This is a an old issue about deduping
attributes, specifically attributes that are added by scopes conflicting with attributes that are later added, you know, via, like the actual log message.
and from a spec compliant standpoint things should be deduped
or there should not. Whatever duplicate keys should not be allowed.
And there's a bit of history on this conversation. But a while ago Steve basically said, like, Hey, you know, I want to play around with like, you know what kind of overhead deduping is gonna
is gonna take.
And
so my understanding is that that's kind of the the main focus. But this pr raises kind of like a
an additional interesting concern. So here's my understanding of it.
Basically this, when you, when you configure, include scopes on the logging options.
there is no way that you can then, via like a processor.
do anything with those scope attributes. It's basically like you enable that thing, and by enabling it, it means those scope attributes are going to get exported.
And I can see how that's somewhat undesirable.
How this is linked to that issue is, I think that they're looking at this as effectively a
a workaround, a temporary workaround, maybe, but I think it's worth talking about.
What should actually happen. So their temporary workaround is like, Hey, let's
let's add this environment variable that essentially allows users to set include scope to true.
thereby allowing scope attributes to effectively like, you know, whatever quote unquote flow through the pipeline, but
disables the actual export of them.
So the Pr is actually relatively small. It's all in the Otlp exporter.
New configuration option. Basically, I mean, it's an experimental one. So it's
actually, he is making it public. So no, this is under experimental options. I think I haven't expanded all this. Anyways, the idea is that this wouldn't be exposed
except via an environment variable. And then this is the crux of it. Basically, it just makes it so that
you have to do something explicit
to actually get those scope attributes on
And so in their example, like
the idea is that somebody could implement a processor that that manually copies scope attributes down.
so I had this other thought that I wanted to pass by folks.
I see the need, the the desire to effectively decouple
like in like including scopes from the exporting of scopes.
and so the thought I had.
and I don't like it because it kind of seems ugly, but I kind of wanted to just put something out there to get a conversation started.
What if we introduced another configuration option called
export scopes, which is defaulted to True.
which means that if somebody sets include scopes to true.
they get the behavior as is today no breaking change. Basically, we just have another. We not have another thing, a new configuration that defaults to true
But then that enables essentially what they're after in this Pr, where they could
set include scopes to true and export scopes to false
thoughts on that.
**Mike "Blanch" Blanchard** 30:44 So I kind of like where you're headed, Alan.
I don't. I don't particularly love the design proposed, because it's specific to Otlp exporter.
It seems like the real need here is I want to have the ability
to do stuff with the scope attributes that's like the underlying thing.
I like your idea of adding an Api putting up a bool like export.
I also don't super love, because then every exporter has to go get modified to respect that flag, and we can't really control it.
I would hate for us to have an option. Users could say, Oh, don't export, but then you use, you know.
whatever Xyz exporter, and it doesn't know about that flag, and they still get exported. But I was kind of thinking as you were talking is, we have.
you know, a function or a delegate, or something that just gets fired in the SDK,
which is essentially like a filter or something for the scope attributes.
so you could just drop in your logic, and the SDK. Would execute that, so that
it works for all exporters. If that makes sense.
**Alan West** 32:11 so.
And and you're, you're suggesting that this this delegate would be
on this class, it would be a, new, it would be a new option on this class.
**Mike "Blanch" Blanchard** 32:20 Yeah, for sure. Go on the the I logger options.
**Alan West** 32:29 And then I guess the yeah. So when would that get executed? Would it get like executed?
I think one of the benefits to
well, I mean, I know. I guess I.
**Mike "Blanch" Blanchard** 32:42 One other option we could do is there is?
There might be. I don't know. I haven't looked at this code in a while, but there's like 2 modes on the log record. There's like
buffered and
just wrapping. The state buffer gets executed when there's like a batch processor in which we will capture everything and like write it to our own pooled like list.
There could be a method here which is, like, you know, invoke buffer or
buffer, something to invoke, so that we capture all the scopes.
I'm not sure if the buffering takes the scopes and the State attributes and puts everything, or if it has its own buffer of the scopes, I'd have to go verify that. But that could also be an option, so that logic would be like you drop in a processor in on, and you call log record dot buffer, and then you'll have everything in attributes, and then you can do whatever you need to do, dedupe, add or remove.
that makes sense at all.
**Alan West** 34:07 Kind of I'm not quite envisioning where that
when when that buffering would happen, essentially
enabling it to be available to a processor.
**Mike "Blanch" Blanchard** 34:26 But you would call it in the processor.
**Alan West** 34:30 Oh, it would be so like in a custom processor. You'd have to do this.
**Mike "Blanch" Blanchard** 34:35 Yeah, you would call, you know, record dot buffer, or capture, or collect, or something.
and that logic would say, you know, if this log record is already buffered, because, you know, it was added to a batch, and it just no Ops.
If it hasn't been buffered, then it calls like there's a method on log record that's called like buffer, and it buffers scopes it. Buffers attributes. It would just invoke that. So that when that call returns
you have all that data, and then you can inspect it. I just don't know if it goes on
2 separate things, or one thing
looks like right there it goes on to buffered scope. So I don't know if there's an Api to get at that data.
So the the function design might be better. In that case
we'd have to kind of look at it and see what we could do.
**Alan West** 35:36 Yeah. Okay.
But then, how would that all? I'm just kind of trying to think about through how all that would work with? The existing behavior, which is kind of entangled with the Otlp exporter, at least, where.
if somebody set include scopes to is is your idea that somebody could set include scopes to false.
which is the default. But then they could still either have a function.
or you know this buffering solution.
**Mike "Blanch" Blanchard** 36:15 And that. But I would.
The I don't think the the ask here is really, I don't want to export my scopes.
The ask here is, I want to
drop some of those scopes. So if you go back to that, the code in the processor.
**Alan West** 36:36 Are you talking this like their example code.
**Mike "Blanch" Blanchard** 36:38 So what they're doing here basically is they're manually looking at the scopes, and they're moving them to attributes.
So they're they're not really asking that scopes are not exported. They do want the scopes exported. They're just exporting them as attributes. That's more of like a means to an end.
They're turning off the export so that they can manually process the scopes and then put them as attributes, and then they export the attributes. They really still want the scopes exported. They just want
not the default behavior.
So I think we could give something more elegant that
accomplishes what they're after, but without having to force exporters to do anything.
**Alan West** 37:31 Yeah, I see what you're saying.
**Mike "Blanch" Blanchard** 37:36 So I think what we should look at is some Api on that ilogger options that allows users to
inspect the scope attributes and add or remove things.
and then you could just let them export.
**Alan West** 37:57 Yeah, yeah, yeah, I see.
Yeah, I like that idea.
Okay, yeah, let me check on that. And then maybe
I'll comment on this. Pr, I think.
I think where they're headed is definitely addressing a legitimate need.
I just would prefer to do something that is actually more official than just just this, so, okay.
**Julius Koval** 38:36 Well, I'm looking at the profiles, and it looks like instrumentation. Scope includes a field for attributes.
so shouldn't the scope attributes be in there.
**Mike "Blanch" Blanchard** 38:57 I don't think the I logger scopes fit naturally into instrumentation, scope.
**Alan West** 39:08 Oh, that's what you're saying. Okay, I didn't quite follow
right? No, yeah. They're kind of. They're kind of 2 different concepts, both with the using the word scope.
The idea of an open telemetry scope is more of like a
more of like
what's a good example like like so like logging like I, logger has the notion of like a naming a logger.
and so like that that that name of the logger is something that
oh, no, no, okay. So I'm I'm actually paging all this back into my head. So there's this
for both for all of this stuff. So tracing.
tracing tracers, meters, and loggers from like an open telemetry perspective.
have a notion of a name, a version which is optional.
and then attributes that are associated with that
thing. And it's basically like, you know, one set of attributes for each of these things tracer, meter, or or logger
from an ilogger perspective, right? Like you can have a whole bunch of like nested scopes, which is something that is
doesn't necessarily like. Have a direct
Oh, analog in open telemetry terms.
So from the perspective of like the the attributes
associated with the scope in ilogger terms.
we effectively just treat those as
attributes on the log record itself?
Does that make sense.
**Julius Koval** 41:07 Yeah, I guess the analogy would be if the if the I logger itself had attributes which it doesn't
right. I guess that would be analogous to activity, sources, or meters? Is my understanding.
**Alan West** 41:31 Yeah.
okay.
So thanks for talking about that.
See if we knew. Where am I at? Here?
Let's go back.
There's 1 other thing I wanted to talk with folks about.
Yeah, it was this issue.
I think this has come up before. But, I don't remember in what context. So
this individual basically wants, right now, when you configure the headers option for the Otlp exporter.
it's basically like a you said it once.
and it's becomes like a static configuration.
They have a use case where they need to
as maybe, like some authentication token expires, they need to be able to update that.
And, Martin, you jumped in here and highlighted
this. Basically, like, right now, the Otlp exporter options don't implement ioptions monitor. Is that correct?
**Martin Costello** 43:14 Yeah, they just use I options. And I options, if I remember correctly from memory is a snapshot. So you it's just like you get it once, and it doesn't change.
**Alan West** 43:28 Yeah.
So I like that. I like that as a thought.
Blanche. I wanted to wanted to get your thoughts on this, too, because you've done so much more work with the configuration stuff than I think anybody else.
What do you think.
**Mike "Blanch" Blanchard** 43:53 I mean, we have the options, monitor. It's all hooked up and plumbed in there.
We just don't do anything with it.
We could.
I sort of always intended it to be
hot, reloadable, just nobody ever asked for it. So I don't have any issue with doing it.
It's just the hard part is.
some things will never be hot, reloadable. So it's more of like a documentation burden to like
correctly know what is and what isn't.
**Alan West** 44:39 Right. So it'd be kind of like an exercise to like. Go over the options and
kind of decide what
what should be changeable, and what shouldn't be changeable. So headers is, of course, the ask
but some of these other things might not be possible.
**Mike "Blanch" Blanchard** 45:01 Yup.
like protocol, I think, is one, because based on the protocol we spin up like, you know, the type of classes and stuff. So, if you like, if that's switched.
we'd have to like tear everything down.
It's possible. But headers seems reasonable, cause like I don't know. You could rotate like a key or something.
**Alan West** 45:28 Right, right.
**Martin Costello** 45:29 Yeah, at the previous employer of mine. Now, production services, we sometimes
have unintended consequences where we had a dynamic configuration store, and people would update values in the dynamic configuration store. The app would reload the settings. But then we'd find that the bit of code that cared about that setting didn't use Options Monitor.
and would never see the changes. So you might, where it was like, completely derailed the point of a dynamic configuration system.
**Mike "Blanch" Blanchard** 46:02 Yeah.
**Alan West** 46:03 Yeah.
Okay. Yeah, that's some good thoughts. I think.
I mean, I think the at the end of the day this issue would be have to be up for grabs. I don't know who, or
might have the bandwidth, but can certainly ask
the person who opened the issue if they wanted to. But if anybody else is interested, I I think this approach is is a good one.
**Martin Costello** 46:44 As I already had to dig into it. If the original author doesn't want to pick it up themselves, then I'm happy to pick it up at some point in the next couple of weeks.
**Alan West** 46:54 Okay, okay, that sounds good.
Yeah. I'll just comment on the issue after after the meeting here, just to come document our conversation.
And otherwise. I think it sounds good.
I think that was the main things from the issues and Prs. I paid maybe less attention to the contribute repository, but we can take a quick peek over there to see if there's some stuff.
Martin. I know you still have a number of Prs out here.
Since you're here, maybe we can just take a quick scan
and see if we can get any of these moving along.
**Martin Costello** 47:41 So just looking at the list. So the artifact type. But I think that's waiting on input from Raj
because he was questioning me, needing to move some of the settings around. I can't remember it was in this repo, the other repo, but I did the same thing in 2 places, and this is dialogue on one of them, where he's questioning how it's set up.
Like the cu. The custom targets that already there sort of go against my understanding of how the artifacts output wants to be defined. So there's like an unresolved question about that one.
And then the only
when that's resolved. The only outstanding question with this we're not outstanding. Question is sort of a bit like
I can't test the publishing part. Still work.
so there may be unsurfaced. Issues created by this.
**Alan West** 48:40 So like the next time we do a release, then we'd have to just kind of work through those, and.
**Martin Costello** 48:44 Yeah, I'm happy to do that if it does happen when this gets merged. But yeah, there's like, there's certain things that I just had to just do like
code searches for terms and hope I've found all the bits.
**Alan West** 49:01 Yeah, that makes sense.
From the like. An end. User perspective, you know. To be honest with you, I've not spent a lot of time like really paying attention to this Pr and understanding really what it is from like an end. User perspective. What? What.
**Martin Costello** 49:15 So to to a consumer of the library through Nuget, is completely invisible.
**Alan West** 49:21 Yeah.
**Martin Costello** 49:22 It's just it's just engineering. Because I made a Pr a few months ago so that the Ci builds, attach the new, get packages to the Github actions workflows. So if you want to play with the Pr you can just download the packages
and then the way that they're currently spread across the repo in different bin folders
means that without custom scripting to flatten the structure. If you just say to Github, Hey, Hoover, up all the nuget packages into artifacts. You get the directory structure mirrored in the artifact
and then in the conversation. For that, I suggested. Well, if we used artifacts, output everything gets put in a single directory so you can just go, hey, get help! Hoover up everything in this one directory, and then you get a flat structure.
But I was putting off doing it
on the basis that I didn't know all the foibles of the internal engineering for the repo, but then it looked like nothing else was gonna happen on it.
So then I just picked out.
however, long ago it was open here.
**Alan West** 50:32 I gotcha, that makes sense.
Does this. So you mentioned like getting the output from a
specific Pr, but does it also influence like, if I were to go here and look at like releases.
**Martin Costello** 50:49 So it shouldn't touch that it, it would only touch it insofar. As the process that makes that happen
is getting the files out of a different directory in the build drop.
but they're sort of the public facing behavior should remain the same.
**Alan West** 51:10 Gotcha. Okay.
**Martin Costello** 51:11 It just makes it easier to author
the build targets and other internal processes, because you can predict exactly where all the files are going to go without having well, and maybe you can do that with the old way. But it's just neater, because, like, there's a single directory in the root of the repo in your local clone, and if you want to nuke everything, you delete that one directory, rather than having to go into all the projects into the all the bin and the objects
it was. It was a new feature added in Donate 8. So it's it's just like
the repo was set up to deal with the ecosystem as it was at the time it was set up.
and a new feature has come along since that makes it a bit easier
to do those things in hindsight, and I've just come along and adopted that in that peer.
**Alan West** 52:06 Gotcha. Okay, I get it. Now.
**Martin Costello** 52:09 Then the next one. You don't need to click into it. But I think I've done for a while in my own repose is as the.net previews come out.
I target the latest preview, run all the tests, see if anything breaks.
and so far, I think, for contrip. So far nothing's broken, but it's just sort of like a background ticking. Pr, that's just adding the net 10 targets. But it did flush out in the
the non contrite repo. There's a breaking change for the W. 3 exporter in.net. 10,
which the W. 3 C. Conformance tests
don't like, so there's like a 1 liner change in the other repo which opt into the legacy behavior switch that they put in for Donnet 10.
But yeah, that's mostly just sort of a background, mechanical boring Pr with the intention that when.net 10 ships in November
we're ready.
**Alan West** 53:16 Yeah, I like it. Okay, great. Okay.
**Martin Costello** 53:22 We've got the test we've already talked about
the Pl. I we spoke of at the top
does. That is that dependable thing we already chatted about
via an issue I think dependable just doesn't seem to properly work if there's more than one image
in there, so it's sort of it's either nothing or half.
**Alan West** 53:47 Yeah, it's basically, yeah, it's it's
yeah, exactly nothing or half. That's exactly what it's doing. I think it. I guess we can just kind of continue to roll with
the behavior, knowing that there's still kind of a
a loose end there, that ideally we have a solution for but half is helpful.
**Martin Costello** 54:14 I think I think at least it doing half
raises the point that there's a new version available, even if it doesn't successfully update it also, it can be just approved and merged in one. Go.
**Alan West** 54:25 Right right, and then prs like this will still require like manual intervention, because it requires the the other half to be resolved.
**Martin Costello** 54:34 Yeah.
**Alan West** 54:36 Yeah, I think that that's
fine for now. Yeah, if you ever do have any other thoughts, you know, this is not something I normally have a whole lot of bandwidth to think about, but you know I'm I'm open to them, but I totally get it that this is probably not like the the thing that's
top on anybody's list.
**Martin Costello** 54:52 I have recently been playing with renovate, which is effectively dependable, competitor and it does neatly do this. It was kind of surprised that a different, not the get up. Blessed product did a better job, but
potentially in the future renovate would do like it gives you one Pr, and it will update the SDK and all the docker files in one. Go.
**Alan West** 55:19 That'd be cool. I'd actually heard a little bit about how the open telemetry Java project has adopted renovate
in order to cut down on the on just the the maintenance kind of toil of these dependabot prs.
so that could be cool.
**Martin Costello** 55:40 But yeah, so
it's it's something to bear in mind for the future, if the way it's doing it at the moment gets annoying. But yeah, I think I think at the moment that Pr is just, it fixes the problem which was the other one, where it was doing
everything to 2 newer version. Now, it's only updating some of it, but it's at the, if if nothing else. It's very crude notification mechanism, if nothing else.
And then the only other Pr I had in the list was the top one from today is just while I was looking at whatever I was looking at earlier, I just found it to do comment in the visual studio task bar that said, when.net 7 isn't used, remove this code branch.
**Alan West** 56:21 Hmm.
**Martin Costello** 56:22 So I did it.
**Alan West** 56:24 Cool. Okay.
Yeah. Great
thanks for walking through this.
I guess at this point last call, if anybody else has anything else, they wanna chat about.
Okay, talk to you all next week.
**Martin Costello** 56:57 Hi! Everyone.
**Alan West** 56:58 Bye-bye.
**Julius Koval** 56:59 Bye.
