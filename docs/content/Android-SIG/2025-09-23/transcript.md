SIG: Android SIG
Date: 2025-09-23
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/439gt3JBDdEt9KZL4GXMcojSK0edDg_Qq3PvzIPiEvtzjpk3nZPOCVqaiM13v--y.Ha9wBTN6QxJuaqG1
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:34 Good morning.
**Jamie Lynch** 00:41 Mine.
**Jason Plumb** 00:42 Using that, very purposefully as a general greeting, knowing that most people, or a lot of people, are… it's not their morning, but here we are.
**Cesar Munoz** 00:53 That's okay. Good morning.
**Jason Plumb** 00:55 Yeah, how's it going?
**Cesar Munoz** 00:58 Oh, good.
**Jason Plumb** 01:01 I am very much not quite awake yet, but… We'll try this.
Yeah.
Alright, I am sharing. Okay, so, Francisco, have you been here before?
**Francisco Prieto** 01:21 Nope, first time.
**Jason Plumb** 01:22 Hey, welcome! Yeah, are you familiar with OpenTelemetry? Have you joined any other SIG calls before?
**Francisco Prieto** 01:28 No, this is my first SQL. I am familiar with telemetry, though.
**Jason Plumb** 01:32 Yeah, welcome. What we typically do is we have this document that is shared from the community page. I can also put it in there, someone can put it in the chat for you if you don't have access to it. Feel free to add yourself as an attendee, and any agenda items, feel free to add those, you know, to the bottom of the list, and we will get to them.
Hopefully this hour.
**Francisco Prieto** 01:52 Nice, thank you.
**Jason Plumb** 01:53 Yeah, welcome.
So, I have been a little bit busy and distracted on other things, and have not been looking at Jamie's pull requests, among other things, but I'm aware that they're there. And yeah, so apologies for being… Multi… multitasked. Constantly.
Let's jump into the first one.
I think, yeah, we're 3 minutes after, let's just start with, this, looking at this one.
There is a CodeCov error in this PR. Okay, ye… I… I did see this.
It's, like.04% or something?
Let's see… Yeah.03%. But also, you still ask a good question, because the code coverage should not be changing on a PR that's just Markdown files, right?
Are we on the same page there?
**Cesar Munoz** 02:52 It's kind of strange. Yeah. I have no… I have no experience with this tool, so maybe it's normal. I realized that I still can merge PRs, because they happen with, yeah, yeah, so… so it's not a blocker at least, but… I'm just curious, because it, you know, it seems a bit strange.
**Jason Plumb** 03:12 And it does show up, you know, it does mark it as, like, a little red portion of the build cycle there, and it does mark it as red here, one failing check, but it's non-blocking, which is what we want. I think we don't want to gate, at least at this phase in the project, we don't want to gate PRs based on that decline, but I think as maintainers and approvers, we should look at these numbers, and especially on code PRs, be sensitive to them, like, significantly dropping coverage. Like, if somebody adds a bunch of code and the coverage goes down by some amount, like, we want to see that number trending upward and not downward as the… Is the main takeaway there.
I can't… I can't explain this.
We can compare… Yeah, we can compare what the base was, like, what this, this, these two, and see if there was another commit that might have snuck in there, like, in between those, is my suspicion.
But, I'm not sure.
**Mustafa Haddara** 04:09 Was the other… was the other PR adding Markdown files?
**Jason Plumb** 04:13 This PR?
**Mustafa Haddara** 04:14 Yeah.
Because, like, I'm wondering if it's just doing.
**Jason Plumb** 04:19 No, it's.
**Mustafa Haddara** 04:20 a really dumb, like, WC-L, and just counting how many lines are in the… everything.
And then our tests aren't covering the markdown, and so it's like, oh, you have more… uncovered lines, because it's all extra markdown lines.
**Jason Plumb** 04:35 I like this line of thinking, I hope that's not the case.
I would not expect it to use markdown files for consideration at all, but I like what you're thinking.
**Jamie Lynch** 04:49 I did notice that this PR is one commit behind main, so I think my theory would be that perhaps it's just comparing, like, against the wrong thing, and in that commit, there was, like, some extra code added or taken away.
**Jason Plumb** 05:04 Yeah.
**Jamie Lynch** 05:06 Buh.
To elaborate on, like, why it's failing, I think there is a code… there's some YAML file that you can configure to kind of, like, change this behavior. So, yeah, maybe I can go away and take a look at that.
**Jason Plumb** 05:27 Yeah, I thought I had CodeCov in the name, but maybe… This one.
Right. Is this the right one? Yeah. No, it's a different tool now, right? It's.
**Jamie Lynch** 05:47 Yeah, it's CodeCov, eGAML, we might not have it defined, but it allows you to override The defaults, which I assume is just what's getting applied to her.
**Jason Plumb** 06:04 This is definitely pre-coffee.
**Cesar Munoz** 06:07 Other orders, and it's also something I'm not familiar with, so that's mostly curious.
**Jason Plumb** 06:12 Okay. So the… so based on what you said, Jamie, if…
**Cesar Munoz** 06:15 this PR… if any PR with this issue just does a rebase, then it should get Did it agree?
Is that in theory?
**Jamie Lynch** 06:25 That would be my assumption, yeah.
I guess we'll see if that plays out in practice.
**Cesar Munoz** 06:33 Got it.
I mean, it's…
**Jason Plumb** 06:36 It, it, that's not…
**Cesar Munoz** 06:37 blocking, so… It's not a plugin, but it is quite strange, so if… I guess, if… I mean, if it's not complicated to avoid this kind of I mean, I would consider this a false… A false positive, a false, you know, I mean, there's really no… reason why any tests should be added into this PR, so… If there's a way to avoid it, that would be nice, but if it takes… if it's too much work, then it's probably not worth it, because it's not blocking, so…
**Jamie Lynch** 07:15 Yeah, I think it's possible to, like, adjust the, kind of, like, sensitivity of… like, when it fails for check, yeah, it should just be a case of setting a field in a config file, so… yeah, I'll take a look.
**Cesar Munoz** 07:32 Thank you.
**Jason Plumb** 07:34 Yeah, I'm not gonna lose sleep over this one, I think this is… this is fine, but I did also, like, when I saw it on the agenda, I did remember seeing this, and I was like, I should… I should go figure out what's up with that, and of course, haven't had a chance to come back to it, so… Yeah, maybe, I mean, we could also consider, I'm assuming it's probably not easier… To even omit the code coverage on PRs that are strictly Markdown, or, like, non-code files. It might be harder, but that is another option, I suppose, is just omit it. Like, don't even bother if it's not code, but… Okay, cool.
Okay, I'm sorry, yeah, okay. I… I have a Jamie here that I work with that spells it the other way, and so I'm gonna keep doing this, and I'm sorry. I recognize it when I'm doing it, but yeah.
Okay, next one. Yes…
**Cesar Munoz** 08:56 Well, you know, once in a while, there are PRs that I guess, you know, the, How would I put it?
Can create some sort of… Based.
Our foundation for… for other stuff.
And I think this is… this might be one of those, so that's why I… thought it was worth, you know, discussing in the SIG meeting.
I like the approach. I think it's aligned with what we discussed in the last SIG, which is, like.
you know, Annotating stuff that we… Don't want users to rely too much on, or to… I mean, stuff that we could break, and that way we avoid I mean, to, you know, keep… pushing backwards… pushing backwards… the release of 1.0, I guess. I guess that's the point, if that makes sense, so… Yeah, I just wanted to bring attention to it.
**Jason Plumb** 10:01 Yeah, this is definitely one I have not had a chance to visit yet, but let's take a look real quick.
**Cesar Munoz** 10:11 And here, it's just creating the annotation, but not using it, right, Jamie? So, it's not like.
**Jamie Lynch** 10:16 But I've used it in one place on the session config class, just to kind of… yeah, demonstrate how it would be used. So, if you have an API for We're not 100% sure, and you can basically annotate it with this incubating annotation, or we can call it whatever we… whatever we want, really. And… At build time, that will show up as a compiler warning, so you'd have to opt in to get rid of a compiler warning.
**Jason Plumb** 10:48 Cool, so that, in practice, it's kind of like the deprecated annotation for Java stuff as well? Like, you get a warning on that, and you can configure it to be a… you can configure it to be an error, even if you'd like, so… Yeah. How does the compiler know about this?
Is it…
**Jamie Lynch** 11:05 So, I think… There is some sort of compiler plugin like, built into Kotlin that would, like, process this annotation and, yeah, then create a… warning, I'm not too familiar on the details of it.
**Jason Plumb** 11:25 Okay. It would be cool to see that in action, because, I'm… I'm also, like, still on my first cup of coffee, but, it's not immediately clear to me how a custom annotation would be recognized on a… Like, the use of a method that is annotated with a custom annotation like this, it's not immediately clear how that would… the compiler would know to flag that as a warning.
**Jamie Lynch** 11:52 Yeah, that is a good question.
**Jason Plumb** 11:56 I like this idea, though. It does send… it sends a very, a very clear message. So this is also… Optin is a, is a built-in.
And so, yeah, this sends a very clear message that you're doing something, like, with intention.
Cool. And so, without this, were you seeing that warning?
**Jamie Lynch** 12:26 Yeah.
**Jason Plumb** 12:26 Oh, okay.
**Jamie Lynch** 12:27 So, it'll show up as a warning. I think you can even configure it to be an error if…
**Jason Plumb** 12:32 school.
**Jamie Lynch** 12:33 if you really want to, but I think a warning is probably a good middle ground.
**Jason Plumb** 12:38 Cool.
Yeah, I think this is great. I think this is really, really helpful.
**Cesar Munoz** 12:58 Yeah, and if it's enabled by default in Android Studio, then it's probably that's enough, I mean, for those warnings to come up.
To show up there.
**Jamie Lynch** 13:08 Yeah.
**Jason Plumb** 13:10 Yeah, it's a little…
**Cesar Munoz** 13:10 OpenTelemetry, now that I… I just noticed that line, OpenTelemetry ROM initializer, my understanding is that it will be, at least so far, the one thing that will be stable.
in a 1.0 version, so that… does that opt in? Yeah.
Yes, they're incubating, yeah.
to it.
**Jamie Lynch** 13:33 Oh, yeah, so one interesting aspect of this is that it does, like, propagate it, so if you're using, like, an incubating API, which OpenTelemetry BOM Initializer does right now, because I've, annotated session config as incubating.
Yeah, it kind of propagates that, so you've got to opt-in on anything that calls it.
**Jason Plumb** 13:56 So it's transitive, you would have to also opt into OpenTelemetry Realm Initializer, then?
Is that what you're saying?
**Jamie Lynch** 14:07 So… I believe if, like, it's an internal… if it's, like, not publicly visible.
then you wouldn't need to, as a consumer of the library, then you wouldn't need to opt-in.
If it is publicly visible, which I think in this case it is, I… Think it would be necessary to… opt-in, Yeah, that's probably something to check out again.
**Mustafa Haddara** 14:39 So I feel like, for this case, then, we would need, like.
maybe two constructors for OpenTelemetry ROM Initializer, one that doesn't use the thing, and then the other that… does… Opt into the incubating.
**Jason Plumb** 14:59 Yeah, I'm not sure on that one, I think what you're suggesting is, is, can we… can we apply this often, then, at a method level as well?
So if we had…
**Mustafa Haddara** 15:11 It doesn't have to be that over the initialize.
**Jason Plumb** 15:13 Yeah.
**Jamie Lynch** 15:19 Yeah, if that should be possible.
**Cesar Munoz** 15:21 Or to a method parameter only.
**Jason Plumb** 15:24 And that would be the only thing.
**Cesar Munoz** 15:26 Only if you add it, maybe.
I mean, I like the idea. I think, ideally, but probably not realistically possible. Ideally, the first version should have… all within that initialized method should be something we're confident about exposing.
So… I bet I don't know if it's gonna be… feasible.
So…
**Jamie Lynch** 15:53 Yeah, agree. I'm pretty open to where we apply this annotation. I just kind of picked session config as a… Yeah.
Something I saw.
Yeah, I don't have as much context as other folks on, like, which parts of the API we feel aren't particularly, like.
Happy with.
**Jason Plumb** 16:17 Do we, on pull requests, still build the demo app?
**Cesar Munoz** 16:24 I think we do, yeah. Yeah, there is.
**Jason Plumb** 16:27 I'm wondering if the demo app is getting a warning By its use of the initializer.
So should we expect to see that?
Would I… would I see it with the speed with which I'm scrolling?
**cleverchuk** 16:47 I'm thinking you wouldn't, because it has already been updated, right?
**Jason Plumb** 16:52 Oh, look! Yeah, yeah, here it is.
That's great.
Is that… is that transitive? Let's see, so… So this is while compiling stuff in… the agent… So, it looks like it's getting anything that touches that session config. Is that… is that what this looks like?
And other classes that are in the same package also have to opt-in then? Otherwise, you get this warning?
**Jamie Lynch** 17:44 I think… I think those classes are referencing for session config in some ha… some… some way.
**Jason Plumb** 17:52 Right.
**Jamie Lynch** 17:53 And added an opt-in.
**Jason Plumb** 17:55 Okay, okay.
**Mustafa Haddara** 17:59 But I would expect… Like, does the demo app not use… the ROM initializer that we were just looking at?
**Jason Plumb** 18:06 It does. That's why… that's what… then that's what I was looking for, and that's not what that was yet. That was just comp… it looked like that was compiling the session.
**Jamie Lynch** 18:14 I think line 19.7 seems to be demonstrating that as well.
**Jason Plumb** 18:20 I'm sorry, which line?
**Jamie Lynch** 18:22 At 927.
**Jason Plumb** 18:24 All the way up, like, scroll up to 97?
**Mustafa Haddara** 18:27 No, you're ahead.
**Jason Plumb** 18:28 at it.
**Mustafa Haddara** 18:29 927.
**Jason Plumb** 18:30 Oh, 927, sorry.
Yes, okay, so… that is in the demo app on line 41, that's gotta be it, right? It's like, hey…
**Mustafa Haddara** 18:43 Yeah.
**Jason Plumb** 18:44 Yeah, okay, that's cool.
That just shows, like, that makes it very obvious.
I think. Let's just put a link to that in here.
So users, I mean, I'm stating the obvious, probably, but, like, users of… the initializer, or of this project at all, would not see these. These are just, like, internal for our own development, and… But does that also then mean, like, this is compiling the session ID timeout handler, which might already be marked in some way as internal?
like, there may not be a public API surface on that at all, but if someone were to use the session ID timeout handler, or attempt to, they should also see this warning, because it's getting the warning. Like, it kind of spiders out through that tree, right?
Like, I don't think the session ID timeout handler has anything… That people should be attempting to use, but…
**Jamie Lynch** 20:03 Yeah, I think I'd need to go away and check on what the behavior is for that.
**Jason Plumb** 20:06 This is already marked internal, like, somebody should not be attempting to use that at all. Or they can't, right? So… But if there were an example, like, if we forgot to flag one of these as internal, then that would probably be the case.
Okay, cool.
Just gonna make one more note about that.
**Cesar Munoz** 20:39 Yeah, I think it'll be nice to see… to have… You know, details of… Different use cases and how it behaves.
Though, one thing I can say is that this kind of approach to dealing with incubating APIs.
I'm pretty sure Android developers are quite familiar with, because Google… uses this approach, at least in Compose, probably other places, so…
**Jason Plumb** 21:11 There's an existing incubating annotation in Compose.
**Cesar Munoz** 21:16 there's… One that reads experimental something…
**Jason Plumb** 21:22 Okay.
**Cesar Munoz** 21:22 I don't know the full name, but I think it's similar to this one.
The behavior, at least.
**Jamie Lynch** 21:30 Yeah, I think there may also be an AndroidX library that lets you pull in an annotation, So that's an option if we want to do that, rather than defining our own, but we could just define our own in one class.
**Cesar Munoz** 21:47 There's one incubating in the Android Reddit plugin.
for Android-related plugin stuff, write-off stuff, but I'm not sure about the SDK. It's probably… There should be, I guess.
**Jason Plumb** 22:01 Is it, is it spelled the same?
**Jamie Lynch** 22:05 I… don't remember what it's called. I think it might be called, like, Experimental, or Experimental API, or something like that.
**Jason Plumb** 22:14 That's cool.
So… Another question about this, if there were… in the near future, when we've hit 1.0, we've got a stable API, and users are using this stuff.
Do we think there's any risk of a user seeing this incubating annotation and start putting it on their own?
Classes, their own instrumentation, and are we concerned about that?
It's like, are we… is it… like, because I'm asking this because it's showing up as an API itself, right? The existence of the annotation is itself being marked as an API.
I don't think we have to answer that question. I just want us to be thinking about it.
**Cesar Munoz** 23:01 No, that's a good point. If it's possible to make it internal and still, you know, get the warnings.
On the end-user project.
It's probably ideal.
**Jason Plumb** 23:15 I mean, that's probably a, like, an edge case, like, I… but again.
**Cesar Munoz** 23:19 Yeah.
**Jason Plumb** 23:20 The whole purpose of, like, trying to get our hands around the size of the API is to limit people doing Odd, unusual things, and this might be one of those cases.
That's not what I did.
Okay, something to think about. I think this is really good. I'm… yeah, I love this. I think this is great.
It also allows us to do things like… just search, like, just find all the things that we've marked as incubating and see what we want to do with them, right down the road. Like, do we want to make this stable? Do we want to hide it further?
Do we want to get rid of it? Like, those questions can be answered once we start using this annotation, so…
**Cesar Munoz** 24:18 Yeah.
**Jason Plumb** 24:19 Cool.
**Cesar Munoz** 24:27 That's all I wanted to discuss.
**Jason Plumb** 24:29 Yeah, that's great. Nothing new has appeared on the agenda. Francisco, did you have anything specific? Are you using… are you using OpenTelemetry Android yet? Are you… Oh, you're with Embrace, okay, so, yeah, okay. I'm finally seeing that, I'm getting, I'm getting caught up. Cool.
**Francisco Prieto** 24:48 I didn't have anything in particular, I just wanted to lurk.
**Jason Plumb** 24:53 Okay, yeah, that's great. That's cool.
Well, We've got a number of PRs, please have a look at them. Reviews are always welcome, and they're very helpful to the maintainers, so please provide reviews.
And if there are issues that are exciting, are there any new ones?
Nothing super, super new.
There's some… oh, what's this one?
That's 5 days ago. I think we can close this one.
Yeah, I think it was a link problem that I think I've since fixed.
Yeah, I think… I think I've fixed this one.
It's in the OKHTTP3 readme.
**Cesar Munoz** 25:46 I remember there was an issue with Maven Central itself. It's not really… it's not this one, or is it?
Because it's an issue that they had.
That we just waited for.
Terrific.
**Jason Plumb** 26:01 Yeah, so this is… oh, it's, it's on the in… it's… yeah, it's this thing. It's like, how to… It's in the installation instructions, where it's, like, the latest version… This one.
Yeah, so I've changed the URL, it's now Sonotype Central.
So, that's how to, like, find out what version of ByteBuddy to plug in. So, this has been… this has been resolved. That link to search.maven is no longer there. I think what happened is, I think search.maven started blocking… you know, as, like, a defensive measure, started blocking requests from GitHub.
Because even when I saw this failure, if you clicked on this in your browser, it works fine.
So, I don't think it was temporary, I think it continues to happen, which is why I changed the URLs. So I'm just gonna mark this one closed.
And I think I can find that PR.
No.
This one.
Yeah.
**Cesar Munoz** 27:11 Aye.
**Jason Plumb** 27:16 Okay.
Okay, cool. Well, it looks like that's what we have on the agenda for today, so we can, stop about half an hour early if, people are into that.
If there's nothing else to talk about?
**Cesar Munoz** 27:40 No, from my side.
**Jason Plumb** 27:42 Cool. I can have 30 minutes to play catch-up on all of these PRs I haven't seen yet.
Alright, thanks, everyone.
Appreciate it.
**Cesar Munoz** 27:50 We'll talk to you later.
**Jason Plumb** 27:52 Bye.
