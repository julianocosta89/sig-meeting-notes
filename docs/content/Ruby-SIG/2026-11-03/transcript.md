SIG: Ruby SIG
Date: 2026-11-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matt Wear** 01:22 Whoa.
**Kayla Reopelle (New Relic, Inc.)** 01:27 How's it going?
**Matt Wear** 01:29 Not too bad, how have you been?
**Kayla Reopelle (New Relic, Inc.)** 01:32 Alright, I was away for a week on vacation, I'm still adjusting to the time zone change, so I'm a little sleepy today.
**Matt Wear** 01:42 F.
Yeah, that makes sense. Hopefully your vacation was good.
**Kayla Reopelle (New Relic, Inc.)** 01:46 It was wonderful, yeah, it was really nice.
This one?
**xuan** 01:56 Hello?
Bye.
**Kayla Reopelle (New Relic, Inc.)** 01:59 Bye.
Okay.
a quorum. I know that Hannah can't make it today, and it looks like Rob's not coming either, so… We might be able to get started.
Yeah, I haven't had a chance to catch up on hotel from last week. This is my first day back.
So, I… Let me know if there's anything in particular that I should take a look at. I'll share my screen for the… Notes, Okay.
Was anyone able to go to the spec SIG today?
Oh no, canceled future today.
**Matt Wear** 03:01 I don't know, there was… there were quite a few things, The first item, if anyone's gonna be at KubeCon, there is a hotel graduation party. You can register for that.
If you wanna go?
This next one, there's this included, excluded selectors for HTTP header capture. That looks interesting.
So I guess this would be for our,
**Kayla Reopelle (New Relic, Inc.)** 03:40 Oh, nice.
**Matt Wear** 03:41 narrative config at some point.
**Kayla Reopelle (New Relic, Inc.)** 03:45 Isn't that weird?
Maybe we can migrate, because I think we have maybe some custom rack header capture configs right now?
So maybe we can migrate to this instead.
**Matt Wear** 04:04 Boom.
Let's see, what else?
there's this instrumentation stability API, It's down towards the end.
dashboard.
First one.
And,
**Kayla Reopelle (New Relic, Inc.)** 04:38 Right?
**Matt Wear** 04:38 I don't know. Basically, people… I have noticed that no instrumentation is stable.
I think this… Oh.
**Kayla Reopelle (New Relic, Inc.)** 04:55 Is that the right one? Is there a different… oh, this one, this makes more sense.
**Matt Wear** 05:01 Yeah, sorry, there's that one.
So I think there's some numbers somewhere of…
**Kayla Reopelle (New Relic, Inc.)** 05:09 Interesting.
**Matt Wear** 05:11 Somewhere I was seeing some numbers of instrumentation that is stable or not. Is it on this one? Look at the rich lift.
Boom.
Yeah, alright. Perpetual, pre-1.0 versions. If we actually look at the files… And if we look at the rich diff on this one, I think it'll be easier on the eyes.
Boom.
So apparently only Java has a couple of instrumentations that are actually stable. Everyone else is…
**Kayla Reopelle (New Relic, Inc.)** 05:48 Mmm…
**Matt Wear** 05:49 is not stable, so… what David is suggesting, if we scroll down to the proposal section.
It's to actually, kind of, at least for, like, the telemetry that you're emitting, having a, A stability that you kind of add to it as you're recording it in code.
And then… having a way for the SDK to set your stability level. So if your stability level is, like, stability stable.
Then all of the things that are, emitted at stability development would just be, They would not actually be admitted, they would no-op.
**Kayla Reopelle (New Relic, Inc.)** 06:30 Mmm.
**Matt Wear** 06:33 It's an interesting idea, I just… I don't know what this buys us in the end.
Oh.
What it would buy us today is if you turned on anything other than, like, development, like, you would get nothing.
And…
**Kayla Reopelle (New Relic, Inc.)** 06:50 Yeah, yeah.
**Matt Wear** 06:52 And I don't understand so much what the transition between nothing and something actually looks like.
To know if this will be useful or not.
But that's… that's the gist of this. It's… it's an OTAP, so he's just asking for some… Feedback on it.
**Kayla Reopelle (New Relic, Inc.)** 07:10 Okay, interesting. Yeah. Yeah, it would be, very all-or-nothing right now for Ruby. And then I guess, too, it'd be… I mean, I haven't read the proposal yet, but if we have, like.
You know, maybe it's… the metrics are stable, like, if our metrics implementation isn't stable, but it's in our instrumentation, do those conventions count as stable or not?
It's an interesting idea, though.
**Matt Wear** 07:39 There's definitely a matrix involved there to figure out how to handle all those things, but yeah, it is an interesting idea.
He also had one about exporter authentication. I didn't look into that all that much, but it could also be interesting.
And then… Ludmila's span type, we've probably talked about this before.
But, yeah, I think… we didn't really talk about this that much, I think it's been talked about previously.
**Kayla Reopelle (New Relic, Inc.)** 08:16 It was just…
**Matt Wear** 08:16 I have a call to look at this and see how you feel.
**Kayla Reopelle (New Relic, Inc.)** 08:21 Okay.
**Matt Wear** 08:23 And yeah, I think in general, it makes sense to put these on spans, and it seems pretty straightforward. You have database spans, you know, HTTP spans.
I think some of the questions in the past were, like.
is this polymorphic? Is your span multiple types? And I think.
**Kayla Reopelle (New Relic, Inc.)** 08:43 Thank you.
**Matt Wear** 08:43 the answer is no, but I think at that time.
there was a question. I could be wrong, I haven't… I haven't followed up on this, Recently, but… I believe it is one… One type per span.
**Kayla Reopelle (New Relic, Inc.)** 09:07 Okay, nice. Yeah, so, yeah, I have a vague memory of this coming up before.
It's kind of more like the semantic conventions type, almost, for a given… Spam.
If I'm remembering correctly, it hasn't changed.
But, cool, that's… that's good to know about.
Anything else on here?
**Matt Wear** 09:31 I think that's it.
**Kayla Reopelle (New Relic, Inc.)** 09:34 Sweet, thank you.
I'll add those.
Links on the queue. Does anyone have any?
Agenda… Topics in the meantime?
**xuan** 09:55 I do have one, questions.
So I, I realize I can use Copilot on any OpenTelemetry repo. Is that, is that, happening to everyone, or just me?
**Kayla Reopelle (New Relic, Inc.)** 10:11 You can't use what?
**xuan** 10:12 I can use the Copilot, pick up Copilot.
**Kayla Reopelle (New Relic, Inc.)** 10:15 Oh.
I haven't tried, personally, so I'm not sure.
**xuan** 10:22 Because on my own personal, ripple.
**Kayla Reopelle (New Relic, Inc.)** 10:26 Thank you.
**xuan** 10:27 use it to, say, let's say, I want to check this PR's file, and then… But any Open.MHU repository is… this is, the copilot is not… is… is unavailable for these people because of organization, policy. I know they changed something for the GitHub co-pilot, but I don't… I'm not sure.
What they changed.
**Kayla Reopelle (New Relic, Inc.)** 10:55 Okay.
Let's see, I don't know, but I can try to find out to get more information.
Is anyone else using Copilot with OTEL, or has run into those?
Okay.
Yeah, yeah, that is… surprising. So, I'll… I'll let you know what I find.
**xuan** 11:28 Okay, thank you.
**Kayla Reopelle (New Relic, Inc.)** 11:39 Alright, so I guess before just… Jumping into the repos… Anything we want to talk about today?
Okay, Let's see… are there any… Top priorities, in the open PRs for folks who are here today to agree this week.
**Matt Wear** 12:20 I got kind of busy, I was trying to go through Schwann's metric PRs, apparently 3 weeks ago, according to GitHub, so I did make a pass… a second pass through the ones I reviewed 3 weeks ago, and I…
**Kayla Reopelle (New Relic, Inc.)** 12:33 Go ahead.
**Matt Wear** 12:34 I have a second chunk that I also need to make a pass-through.
So I was gonna try to do that.
Next.
**Kayla Reopelle (New Relic, Inc.)** 12:44 Yes.
**Matt Wear** 12:45 this… API and Raptor, issue, and I really wanted to, like.
sit down and try to understand everything about Raptors and OTEL, but I feel like this is a project that I don't… I don't currently have time in my schedule or brain for.
But would like to make some at some point.
**Kayla Reopelle (New Relic, Inc.)** 13:07 Yeah.
Yeah, those are… both similar.
Those are thoughts on my end.
Yeah, it's.
**Matt Wear** 13:19 If there's anything else I should have my eyes on, please let me know.
I did open this PR for adding declarative configuration for meter provider. I feel like, I did it for… for logger provider. I just feel like our metric stuff… I think the TLDR is declared a config for meter provider, a lot of things. You try to configure, you'll get a warning saying you cannot configure this.
**Kayla Reopelle (New Relic, Inc.)** 13:43 Hmm.
**Matt Wear** 13:46 Which is maybe okay, but maybe, maybe it makes sense to hold this until most of the things are configurable. I'm cool either way with it.
I was just doing some stuff, for dash zero around declarative config, and I was trying to… upstream everything I could.
So, you probably saw, like, a handful of Of things come through. And this is… This is one other thing, it's like… I… for Lee Stash Euro, I'm allowing, You know, declarative config for things that exist for metrics, and warning on things that don't yet exist.
So… So we can decide how we want to actually handle this, but… If we're cool with the partial implementation, that we should go forward with it, or if we want to wait for it to be a little more fully baked.
Oh.
that I… then I'll just update… update that, you know, as, as things… Come together.
**Kayla Reopelle (New Relic, Inc.)** 14:55 Bart, are you using metrics? I'm gonna put you on the spot. Do you have an interest or a preference for config, declarative config?
**Bart de Water** 15:05 We are using metrics, just sort of like our homegrown stuff so far, which is just, like, directly in the code, I have not used declarative config anywhere yet.
**Kayla Reopelle (New Relic, Inc.)** 15:24 Okay.
**Bart de Water** 15:28 But it might be useful to look into, because our OpenTelemetry initializer in our Rails app is getting a bit unwieldy.
**Kayla Reopelle (New Relic, Inc.)** 15:36 Yeah, it's still, you know, experimental. I think we have a decent amount of things to… Work through it on. But, Yeah, if it's… if it's a project that you're interested in… in looking at, We'd love to hear your feedback on it.
**Bart de Water** 15:56 Yep.
**Matt Wear** 15:58 Yeah, and I'll probably have more to say. I know we're trying to get it in a state for dash zero customers, but I don't Actually using it yet, so…
**Kayla Reopelle (New Relic, Inc.)** 16:06 Hmm.
Okay.
**Matt Wear** 16:09 there may be more… more work to come, but that's good. It's always good to have, Some first people using it to, get it user-ready.
**Kayla Reopelle (New Relic, Inc.)** 16:18 For sure.
Yeah, I think… As long as the warnings wouldn't necessarily block someone from setting the value, like, through the environment variable, or through… you know, an API in the case of if there's, like, some incomplete view instrumentation, then I'm… I think we release it with the warnings, and then make sure that we follow up.
as those other PRs get merged, maybe by tracking things through tickets, but… If it's easier, and we don't think… Anyone is going to… be using it straight away. It looks like there's, you know, only maybe 3 more PRs that we'd want to get merged before this would be unblocked.
So, we could look at trying to prioritize those 3 PRs this week, and… then, That kind of reduces some of the warning questions.
**Matt Wear** 17:20 Yeah, I think we'll still… we'll still have some things at warn, so, I think both of those make sense, but if… We want to prioritize the things that are there, and then get this updated, that's fine, or just kind of merge this, and then, add the updates as they come. Either one works, I guess.
**Kayla Reopelle (New Relic, Inc.)** 17:43 Okay.
Yeah, I don't… Feels strongly either way, mmm, yeah, maybe we… Yeah, I don't know.
let's leave this open. It feels easier for me, at least right now, to kind of track that these things are in flight and could be added to config. I think it might be harder to follow it.
In a separate issue, So, how about we leave this open and keep working on these, and if it's still… those PRs are all still open next week, we could merge with, With the warnings?
**Matt Wear** 18:27 Sounds good to me, I guess… One question, while we're talking about next week, like.
**Kayla Reopelle (New Relic, Inc.)** 18:35 Hmm.
**Matt Wear** 18:35 Are people gonna be at Kukan?
**Kayla Reopelle (New Relic, Inc.)** 18:39 Yeah, I'll… I'll be there, So, it might make more sense to cancel for next week, like a lot of the other hotel… Things are doing… Has anyone else gonna be there?
**Matt Wear** 18:53 Yeah, I'm also gonna be there, so not here, so I would be for canceling.
**Kayla Reopelle (New Relic, Inc.)** 19:10 Okay, I guess, yeah, let's… let's cancel next week.
And we'll chat about KubeCon, KubeCon, when we're back.
So maybe the following week, not next week, but the following.
Into… post… In command… a plan.
Sound good?
**Matt Wear** 19:50 Sounds good.
**Kayla Reopelle (New Relic, Inc.)** 19:52 Great. Alright. Thank… I might add a comment to the Raptors.
Ticket, just so the person knows that… It's kind of a lot to take in right now, but we're interested.
**Bart de Water** 20:14 I don't know how close people have been following Rails development, but I also know that the same team at Shopify is also pushing Raptorization of Rails forward.
**Kayla Reopelle (New Relic, Inc.)** 20:26 Mmm…
**Bart de Water** 20:28 Like, they do want to sort of, like, have the… You know, the best of both worlds of, like, true parallelism, which right now would require forking your web server process, but having it all in the same, like, existing process already, so without the overhead that you would have, even with copy and write.
**Kayla Reopelle (New Relic, Inc.)** 20:47 Mmm.
**Bart de Water** 20:49 At least that's my layman's understanding so far.
**Kayla Reopelle (New Relic, Inc.)** 20:52 Oh, yeah.
That's hopeful context.
It is an interesting idea. It's an idea that, Aaron Patterson brought up at a conference I saw him at in October of last year, something that they were hoping to do and interested in doing, and thinking that instrumentation would be a good place to get the performance benefits from it.
But it's been so long that, yeah, I think I need to learn all about it again.
**Bart de Water** 21:24 I, I can share a blog post on the Slack for you.
**Kayla Reopelle (New Relic, Inc.)** 21:30 Okay, thanks.
**Bart de Water** 21:33 Bingo.
**Kayla Reopelle (New Relic, Inc.)** 21:38 All right. Oh, thank you, I see that.
Alright, Bart, you have the PR open, would you like to chat about it?
**Bart de Water** 21:51 Yeah, two, actually.
**Kayla Reopelle (New Relic, Inc.)** 21:53 Oh, too, okay.
**Bart de Water** 21:54 Yeah, one for Rack, one for Action Pack. We got hit by, like, a bunch of bots yesterday trying to sign up and probably defraud us one way or the other.
And while we're investigating, I realized that we're not actually getting the, request IP on the spans.
**Kayla Reopelle (New Relic, Inc.)** 22:15 Which.
**Bart de Water** 22:16 which sort of, like, hampered our ability to quickly correlate that, like, yes, all these requests are coming from the same IP and, you know, like, go into Cloudflare and get them blocked.
So I worked around it in our app, but I'm trying to be a good open source citizen and also contribute those things back. So… kind of, like, depends on whether you're running something like Sinatra, or Hanami, or, you know, something directly on rack, for which SPR provides the fix.
Or if you're on Rails, Rails adds a remote IP to the request object, and that has its own configuration for designating trusted proxies like Cloudflare or your AWS load balancer, so that it correctly picks up from the X-forwarded 4 headers.
**Kayla Reopelle (New Relic, Inc.)** 23:04 Hmm.
Okay, great. Thank you for opening this. I… I don't have any… immediate concerns looking at it.
That I can take a look this week.
And then… action pack?
So this is to cover the rails side of it.
**Bart de Water** 23:27 Yep.
**Kayla Reopelle (New Relic, Inc.)** 23:28 Sweet.
Alright, anything else in… contribute. We'll renovate.
Underground?
Max Anthropic version, I'll follow up on that. I think the only open question on this, unless there's been a new review.
was, adding the semantic conventions or not.
As the constants in the file itself.
I think… I'm leaning more towards just merging it without that, but, I wanted to bring it up to see what other people thought. Hopefully I haven't brought this up before, it's been a little bit scattered lately.
**Bart de Water** 24:50 I'm… not… I… I'm okay with that, like, it's not code that I'm super, like, you know, working with or looking at anyway.
We want to clean that up later. I don't think that should hold this up right now. I'm excited for this to land, and just sort of, like, metrics getting more stable and mature.
**Kayla Reopelle (New Relic, Inc.)** 25:09 Okay.
Sweet.
maybe then it's just… we can get that out there, so people can start using it, and I can refactor it later on, if we want.
That's all I was… I'm interested in here… it looks like we have a PG fix.
And S&S topics, as well, to take a look at.
Did we do some work on prepared statements before? I have a vague memory of this.
Maybe it was with MySQL, though?
**Bart de Water** 26:22 Trey, what was that? I didn't quite catch it.
**Kayla Reopelle (New Relic, Inc.)** 26:26 Oh, I'm sorry, have we done prepared statements for MySQL? If anyone is aware, just, I can look them up as well.
Oh, it does look like my internet is degrading, so… I'll just keep going. Anything on auto instrumentation right now?
**xuan** 26:56 Yeah, so, there's one thing, about, the Priva, Meetings Court, which I, I forgot is for, for those, Alpine.
Kind of a darker image.
So… yeah, so adding those to support, Alpine alpine Mage.
**Kayla Reopelle (New Relic, Inc.)** 27:29 Nice.
I suppose our Renabox, And then… where are we at with this PR? What do you think about it?
Are we still working on, kind of, getting the initial scaffolding out for users?
Or, are we ready to continue with this one?
**xuan** 28:03 I'll take… I'll take last look, and then… If not, you know, I can't, I can't march to the…
**Kayla Reopelle (New Relic, Inc.)** 28:11 Okay.
**xuan** 28:11 And then… Along with those, darker image, then we can have our new race.
Image, yeah.
**Kayla Reopelle (New Relic, Inc.)** 28:20 Sounds good.
Alright, well, that's a good… bit of information. Is there anything else that people want to discuss this week?
Okay, cool. Well, thank you everyone for coming, and I'll see some of you at KubeCon, and the rest of you the following week.
**Bart de Water** 29:00 Enjoy the conference.
**xuan** 29:03 Thank you. Bye.
