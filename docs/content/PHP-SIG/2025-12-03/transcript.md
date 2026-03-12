SIG: PHP SIG
Date: 2025-12-03
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak** 00:40 Hey, Mom.
**Bob Strecansky** 00:41 Good morning.
How are ya?
**Pawel Filipczak** 00:45 I'm okay. How are you?
**Bob Strecansky** 00:48 Doing alright.
**Pawel Filipczak** 00:50 Good to hear that.
**Bob Strecansky** 00:52 Yeah.
Are you getting into the frozen tundra for the winter yet?
**Pawel Filipczak** 01:04 You know… I'm not sure of which… part of the year it is.
Two weeks ago, it was almost, you know, a summer, now it's… it's foggy and cloudy and quite depressive outside.
**Bob Strecansky** 01:19 Aw, man, I feel your pain.
**Pawel Filipczak** 01:21 Yeah.
**Bob Strecansky** 01:22 We've also had, We've also… we've had some really ridiculous weather. We had 25 two weeks… 25C 2 weeks ago, and now it's zero.
**Pawel Filipczak** 01:34 Man.
So it's… It's called Hero Simiro.
**Bob Strecansky** 01:39 Boo!
**Sergey** 01:41 Alright, guys.
**Bob Strecansky** 01:42 Lude.
**Sergey** 01:42 Your zero or out zero?
**Bob Strecansky** 01:45 The World Zero, not Freedom Unit Zero.
**Pawel Filipczak** 01:49 Hmm.
Is it easy for you to convert it in your mind?
**Bob Strecansky** 01:57 So, I, A while ago, I sent my car to 24-hour time and, Celsius temperature, because I realized that the rest of the world does that, and just because the rest of the world does it doesn't mean… or, like, it's probably a good thing for me to understand, and now I, like… I don't even have to think about it, I just, like, know what the conversion is in my head, approximately, roughly.
**Pawel Filipczak** 02:21 But you're talking very young.
**Sergey** 02:22 14 hours, right? You're not regenerated 24 hours, like, you originate… I'm a… I'm in time.
**Bob Strecansky** 02:27 Oh, I like to… I actually…
**Sergey** 02:29 15 hours. 1500. 1400.
**Bob Strecansky** 02:31 I like that a lot better. The only thing that y'all can't get me with with European is the backwards date thing.
**Sergey** 02:41 Yeah.
**Bob Strecansky** 02:41 This… this tricks me up, right here. This is… this is goofy to me. It should be… oh, I'm sorry, I'm not sharing my screen, I'm just pointing into the void, one second.
**Pawel Filipczak** 02:50 So you mean that if placing here in front is… Bat idea?
**Bob Strecansky** 02:57 That's how… this is how I would put today's date.
Rather than this.
**Sergey** 03:02 No, this… no, this is not good. Like, the whole point why you put months in front is when you sort it as text, then the later date will be later, right?
**Bob Strecansky** 03:12 I'm not saying…
**Sergey** 03:13 go all the way and put the year in front, like, then you will even… if you have different years, it will be sorted correctly. Like, if you're already putting something in front and put the day in front, right? Like.
**Bob Strecansky** 03:24 I'm not saying it's… I'm not saying it's rational, I'm just saying it's what I'm used to. Why would you… why would there be 5,280 feet in a mile? I don't know, it's just what it is.
**Sergey** 03:34 But, so Europe… what Europeans do, they put day in front, right? Then months and year? Is that…
**Pawel Filipczak** 03:40 Yes, yes, yes.
**Sergey** 03:43 Okay.
**Pawel Filipczak** 03:44 Daeman here.
**Sergey** 03:46 Yeah.
**Pawel Filipczak** 03:46 But when I'm doing something in my computer that I'm placing here monthly.
So it's in opposite, right? So it's in reverse, totally, but American style, I mean, the day in the middle, so it's totally out of my brain, so I'm always, you know… even if I know that Which format it is, then, you know, trying to convert it automatically in my brain, it's very difficult for me.
So, I guess for the Americans, it's the same, right? In the opposite.
**Bob Strecansky** 04:22 Yeah, it's… I think it's just what we grew up used to.
But, whatever.
**Pawel Filipczak** 04:27 How is it working in South America? I mean, Mexico, for example, is it the same style?
As in what?
**Bob Strecansky** 04:34 I'm sorry, say it one more time? South America?
**Pawel Filipczak** 04:36 Yes, in South America. Which format are you using?
**Bob Strecansky** 04:40 I think that… I think that North America is the only one that does goofy things with everything.
**Pawel Filipczak** 04:47 Yeah.
**Sergey** 04:48 I think, officially Canada switched to metric, but I think when they're interacting with states, they still might use, imperial system, right? Or whatever that system is called, Freedom, because it's not exactly imperial.
**Bob Strecansky** 05:01 And don't even get me started with time zones and daylight savings time, but that's… Alright, I don't want to… like, let's have a good meeting, I don't want to be angry about this. I do have a… I do have a hard stop at 8.30 today, because I have another meeting, but we can get through all the things that we need to talk about today. Chris, it looks like you have our first agenda item.
**Chris Lightfoot-Wild** 05:24 Yeah, I think this was, something that sort of briefly touched on last week, but obviously you were off, so we said, let's, Let's maybe just get your opinion of it as well, because I don't know if it's something that's… Maybe insight from other things would help with.
But looking back through some of the PRs and issues on the board, where, you know, people are sort of… maybe requesting help with stuff, or… and we're a small pool of people, and it's actually quite poignant, because about an hour ago, there was a PR merged in OpenSeometry I.O, I don't know if you'd seen it.
Because they appear… It was, it was tagged.
**Bob Strecansky** 06:02 Oh.
**Chris Lightfoot-Wild** 06:03 And soon.
**Bob Strecansky** 06:04 do.
**Chris Lightfoot-Wild** 06:05 Pinalto tweak instrumentation.
**Bob Strecansky** 06:08 Neat.
**Chris Lightfoot-Wild** 06:09 Accepted into the registry.
and someone suggested in that, sort of, PR review that, oh, maybe this should be, sort of.
put into the Contrib repo, but then it was just, like, merged as is, and the person sort of said, oh, yeah, I've done the work now, so if anyone wants to do that work and accept it into Contrib, then fine.
So I guess it was more, like.
Going forward, is there any way to try and… attract more contributors in some way, like.
**Bob Strecansky** 06:37 Ina.
**Chris Lightfoot-Wild** 06:38 You know, I would love…
**Bob Strecansky** 06:40 to do that. I mean, I've worked on this project for 6 years now. I would love… trust me, I would love nothing more than to have More active contributors, but it's very difficult to get them.
**Chris Lightfoot-Wild** 06:52 Yeah, absolutely, I just wondered if everything is struggling, or, like, are we not doing…
**Bob Strecansky** 06:57 I think… I think it's… I think it's a dangerous combination of the above.
PHP is not known… like, PHP is definitely not known for its instrumentation.
like, compared to some of the other SIGs, it's not as used for, like, specific development patterns that would lend itself to observability. Like, PHP's main… main, meat and potatoes is web, which makes observability a little different. I think there's not a lot of people that have a cross-section of interest between OpenTelemetry and PHP, so I think that that's just, like, a very weird… like, a small grouping of people that share that interest.
And realistically, the only contributors I think we've ever really seen are people… are companies that are, like, not necessarily mandating, but asking developers to help, so… I… yes, Chris, I agree with you, I think it's bad, and I would love to improve it somehow, and I would love… I would be very happy to field any ideas on how we could make it better. I've solicited Discord groups and PHP mailing lists and, you know, the PHP Fig channel, and all these other avenues that… I feel like we should be able to get some engagement from, but just swinging and missing.
**Chris Lightfoot-Wild** 08:13 Cool.
**Sergey** 08:14 I mean, we had in mind, maybe… I know that Laravel has alternative ways together.
Telemetry, maybe we can, get some bridge with them, and see if we can cooperate in some way.
But, Yeah.
We had something in mind, we have some people that we know that… What is the main… how… what is the name of the main guy in Laravel? Atwell? Something, right?
**Chris Lightfoot-Wild** 08:40 Taylor.
**Sergey** 08:41 Hey, look, they look at all.
Yeah.
Yeah, so… So maybe, maybe we'll reach out, see if we can… we had some kind of plans to do that, but, yeah.
Because I know that, recently I heard that, even though PHP is a little bit… becomes less popular, but Laravel kind of, like, gains in popularity, it's a specific example of, you know, all-in thing, so maybe that's the way, maybe engage more with Laravel community.
**Bob Strecansky** 09:13 I think that that would be… I think that would be great. I think anywhere we can… further engage with the PHP community is a good thing.
**Sergey** 09:23 Yeah, but let's keep in mind, let's see… maybe we need to gather some kind of, like, momentum, have a kind of, like, thin… Work in, and you know, work out all the kinks, and maybe… It will be more of a flying wheel effect from there.
But, I wanted to see him.
**Bob Strecansky** 09:41 I think that would be great.
**Sergey** 09:43 Hmm.
**Chris Lightfoot-Wild** 09:44 If a hotel gets, like, mentions at, like, the KubeCon stuff, is there ever, like, you know, not flyers, but, like, hey, we're always looking for assistance if anyone's interested. Like, does it get, kind of.
Not pushed hard, but like… Is it…
**Bob Strecansky** 10:02 Like a wave down?
**Chris Lightfoot-Wild** 10:05 Yeah, like…
**Bob Strecansky** 10:06 my code.
**Chris Lightfoot-Wild** 10:06 what… That's right.
**Bob Strecansky** 10:09 I didn't see any when I was at KubeCon this past time. There were plenty of observability tracks.
And I think that… We could probably get, like, we could probably find a way to speak at one of those observability tracks to… gained some traction for our SIG, but again, I think… I don't want to say that we shouldn't do it, because I think that we need to keep pushing on this if we want to keep this project rolling.
I'm just saying that I'm tired, and I've tried to do that for a very long time now, and I have been met with a lot of resistance and a lot of non-response, so… Any way y'all want to try and engage with the community, I'm very happy to help, I'm very happy to push forward, I'm very happy to, be a part of.
**Sergey** 10:52 I will see, maybe. We attended Laravel Conference in the past, I don't know. Back then, OpenTelemetry, I think it was about 2 years ago, right, Pavel?
So maybe we will ask our management to also attend, maybe?
in near future, attend one of the Laravel conferences, see… see what other PHP conferences we can attend, and have a booth, and, yeah, we'll see.
**Bob Strecansky** 11:17 That would be cool.
**Pawel Filipczak** 11:19 Next round of Laracon is in March, so maybe…
**Bob Strecansky** 11:23 Nice.
**Sergey** 11:24 Yeah, let's talk with management, we'll see if we can, maybe set up a… have a sponsors, have our company sponsor that to have a booth there that we can… Talk about telemetry with people, yeah?
**Bob Strecansky** 11:37 Very… that'd be very cool.
Alright, any other agenda items before we start walking the boards?
**Chris Lightfoot-Wild** 11:52 Oh, so, can I… Justine, I've left semi-unmaintained in, like, quotes, just to, expand on that very, quickly, sorry.
**Bob Strecansky** 11:59 Sure.
**Chris Lightfoot-Wild** 12:00 I've seen, like, hotel collector repo. Like, they have, like, various components that… and I don't know what the sort of methodology is, but they move through various phases of it being, like, maintained by a subset of people, and sponsored by companies, etc.
So, you know, if it drops off, there's no maintainers, eventually deprecate it and just remove it, because…
**Bob Strecansky** 12:21 Yeah, I think… I think we'll have, we'll have to… Yeah, we'll have to get to that pattern at some point. I think there are, There's probably way… there's probably way too many… Unmaintained.
**Chris Lightfoot-Wild** 12:33 It's much bigger than our stuff, isn't it? Like, it's…
**Bob Strecansky** 12:37 No, oh my god.
**Chris Lightfoot-Wild** 12:37 Yeah, that'll…
**Bob Strecansky** 12:38 They're all much… they're all much bigger than our thing, yeah, for sure.
**Chris Lightfoot-Wild** 12:41 Yeah.
**Sergey** 12:42 I was always wondering, like, what is the advantage of having it all in monorepo versus just having people maintaining their own repos and just keeping some kind of, like, central register and link into that. I mean, because eventually I would see if you wanted one repo, probably because if you're changing anything, then you will automatically refactor the rest of the code. But if people don't do that, why would they want to, like… If you're not going to… if you're not going to be maintained as one piece, like SDK is.
What is the advantage of keeping all of it in one repo, if… opinion.
**Bob Strecansky** 13:16 I think it's mostly for, I think it's mostly for, cross-collaboration and understanding, right? Like, right now, if I want to go and look at OpenTelemetry Collector Contrib, I can see all of the different Contrib packages that people are contributing. I can, like.
garner some information from that when I'm working on my integration. For example.
like, let's just say Datadog does one thing, and then New Relic does another thing, and then… Splunk does a different thing. At least they all have each other for reference in this repo, like, oh, I wonder how they're… I mean, I'm sure you could do that in multiple repos and link them together, but I'm sure I have… a very strong feeling that the contrib… like, I wasn't part of the GC when they created the contrib… repost for each, but my strong assumption is that it's for… mostly for discoverability.
**Sergey** 14:09 Okay.
Yeah, I guess, I mean, if it works… I mean, yeah, I mean, whatever approach is working, like, so… so, Chris, are you saying we should take approach, like, so different pieces will be marked as kind of, like, there will be some kind of, like, stale marking that then it is kind of, like, expunged?
**Chris Lightfoot-Wild** 14:26 I wasn't really… Yeah, I'm not sure that, obviously, we've got, like, such a small set of, auto-instrument packages that we start killing them off or anything. I just… where there's, like, a PR where someone's asking about, you know, something specific, and… No one's kind of… there's no designated maintainer or something for that bit of the system, and it's kind of like, figure it out on your own.
It's strange when it looks like it's under our umbrella, open telemetry packages, but we, like, put you on your own with it.
**Bob Strecansky** 14:58 I think, yeah, I have a strong feeling that this is… this is not a problem unique to us. This is definitely something that other SIGs are having a problem with, and I also think that it's very, Very prudent to… I wish we had something equivalent to, like, a code owner's type file, so that you could say, like, hey.
Bob from Intuit, the part of this package that you're maintaining is, not compliant anymore, you know what I mean? It's like, it would be nice if there was a way we could… have ownership and accountability for the different parts of Contrib. At least so that people… I'm sure that people, like, are blissfully unaware that they're… contrib package is no longer relevant, you know what I mean? It's like… Chris works on, you know, the Laravel Contrib package, and then it's like, oh, works for me, I'm using this the way that I want to use it now, and then you just, like, don't think about it for 3 years, and then after those 3 years, you're like, oh man, this thing is so out of compliance, or oh, so, you know, whatever, it's like… I think that… I wish that there was a better way to do that. I mean, right now, you can, like, go in and look at the git blame and try and associate that with an email address, and then hope that you can get in touch with that person.
To me, there needs to be a more systemic method for long-term ownership. This is probably worth bringing up in the maintainer's meeting, and I can do that next week.
**Chris Lightfoot-Wild** 16:24 Awesome, thank you.
**Bob Strecansky** 16:30 You got it. I will make a note about that.
**Pawel Filipczak** 16:40 And I also see… contributing the instrumentations for the PDO, Carol, and MySQL, I wanted to add myself and Sergey as some maintainers of that package, so maybe we should, you know, try to convince people just to… to put themselves into the README.
It'll be better, you know, at least if someone would need some assistance, help with the instrumentation, then have some contact to reach out, but now… It's… it's… it looks, like, a bit of abundance, so someone needs to look at it and… and try to, you know… To force himself to work on that, but if there is contribution from someone else, but if we're just trying to convince people to… To be responsible for that, so it will keep us together.
**Bob Strecansky** 17:35 Very important to have a cohesive unit, for sure.
Okay.
Oh, I… I have an update, too. I started walking through all those Renovate and Dependabot dependencies. I'm almost done with that. I got the ones for auto-instrumentation, and the root package, I am actively working on the ones for contribib. There's some sort of fan thing, I think, that needs to be fixed, and I will continue to look through that, but… No new updates for that. I think Renovate is definitely the bot that we're going to use. I'll probably… once that work is completed, I'll probably remove Dependabot from our three repos, just because we'll use Renovate for all those updates.
**Sergey** 18:20 you consider automating this whole thing? Like, what is the criteria that you use to evaluate if you want to merge certain things? Is that something that can be automated? Like… You just look at it, it looks okay. Is it more of an art than, of a… Engineer a thing, or…
**Bob Strecansky** 18:39 I think that it's not an art. I think that as I was reviewing over the last two weeks, as I was looking at the PRs that Dependabot and RenovateBot were making, the Renovate output is much more clear and concise and easily rockable and understandable.
And so, that was my impetus for choosing that. They seemed like they were producing relatively similar outputs, so…
**Sergey** 19:02 I mean, in the future, do you think it might be worth… oh, it's not worth even, because it's not that frequent, to even have it reviewed by some other bot and accept.
**Bob Strecansky** 19:12 Oh, I see what you're saying, like… so to… I think that…
**Sergey** 19:18 If it's not something that is, you know, you need to spend a lot of time, then maybe it doesn't matter, but…
**Bob Strecansky** 19:23 Oh, so I… so I agree with you, Sergey. I think that being able to, like, auto-merge those if they're green would be… Fine. I think the frequency in which they are opened is not… It's not.
**Sergey** 19:38 That's why, essentially, I asked if it's an art… how did you… what criteria did you use to evaluate if those PRs are okay, right? If you use something that can be automated, then maybe it should be automated.
Is there something that can be contributed by putting a human in that, in that circle… in that circle?
**Bob Strecansky** 19:55 It's like… it's like that old ex-city, the juice for automating that is probably not worth the squeeze, and it's probably… it's probably worth having just, like, a tiny bit of human intervention, at least for now, just… to make sure that nothing absolutely bananas is going on, you know what I mean? It's like, okay, when I approve… like, it is annoying to approve those PRs as they come in, because, you know, there will be, like, on the order of magnitude of once per week.
But you can also make sure that it doesn't just, like.
spam a bunch of garbage in, or, you know, like, that… it seems like a reasonable thing, or… I don't… I don't know, but… I'm…
**Sergey** 20:32 I was just under the impression that maybe it's too… it's a lot of stuff to review, but you're saying it's not that much.
But, yeah.
**Bob Strecansky** 20:42 Definitely not enough to… once it gets to that point, I'll definitely consider automating it. I don't think it's worth doing now.
**Sergey** 20:50 Okay, sounds good.
**Bob Strecansky** 20:51 Yep.
Really.
I finished, babies.
And equivalency orientation.
I don't really depend on it.
Bye.
15… We'll consider auto-making in the… Future… Yeah, maintenance.
gets unwieldy.
Alright… Let's take a quick look at the board, we got 10 more minutes.
Those are just bought.
Chris, it looks like you had, Composer backwards compatibility for PSR log open. Are you still working on that?
**Chris Lightfoot-Wild** 22:02 I've got comments on both, like, it's on me to just come and pick up, so I'll… I've not had time yet, but I will, Okay.
**Bob Strecansky** 22:10 No problem.
**Chris Lightfoot-Wild** 22:11 Thank you.
**Bob Strecansky** 22:14 Contribute… Looks like they're… this is an open PR that I got a review that happened 20 hours ago, so I will take a look at that later.
And these are all just… depend a lot and renovate, so those I will look at later.
Let's take a look at the… Project board… Which I don't think we have any updates on… Yeah, nothing crazy… Nothing on SDKv2 roadmap.
And then… 25 million installs, that's great.
Alright, let's take a look at the open issues, too, see if there's anything that's… Relevant… Oh, this is related to that PR that's open right now, so… Looks like he has a PR that fixes this issue.
Nope.
Nothing else within… anything reasonable… 3 City and Sveni… Yeah, so this one is…
**Sergey** 23:51 Boop.
**Bob Strecansky** 23:52 Anything else anybody want to cover today?
**Sergey** 23:56 Small question, how much do we have 5 minutes left for your time? Yep.
**Bob Strecansky** 23:59 Yeah, 5 minutes.
**Sergey** 24:00 We were just discussing an interesting feature that we had in Classic, and this, I wonder if you guys encountered anything like that. So, let's say you have a company that provides a service.
And people that use your service, essentially, they themselves send you requests that already have some… this trace parent header in them.
Because they themselves use some APM or even open telemetry system, but obviously, now you cannot continue the trace, right? Because otherwise, you will continue from a place for which you don't have a head of the trace, right?
So you would probably like to restart an entry to your org.
So I was wondering if you ever encountered this kind of use case, and you had some solution for that?
did I explain, clearly, what do I mean by this use case?
What is the problem?
**Chris Lightfoot-Wild** 24:50 Nope.
**Bob Strecansky** 24:51 Let me explain it back to you to make sure that I understand it even more so. So, you, like, let's use our companies as examples, just because that makes it easy. I… I am into it. I create… or I, like, do something, and I have a trace with a bunch of spans in it, I pass that to you at Elastic, and you want to attempt to continue my span, or my trace, or you want to do something else with it?
**Sergey** 25:16 Let's say you are into it, and you're now integrating… you provide an API to your external customers, right? You have customers that pay for using your API, they send you requests via this API, and you would like to obviously collect telemetry on your processing of those requests, right? Inside Intuit.
But sometimes the requests themselves will contain trace parent, right? They will themselves already come from a client that also uses some APM solution.
**Bob Strecansky** 25:43 Hmm.
**Sergey** 25:43 that, obviously, you cannot continue the trace, because then you will not have the head of the trace. So you would want to restart it, right? That probably would make sense. Also, you probably would not want to rely on the sampling decision and all that, right? So whatever comes as a transparent.
you probably would not want to trace state, even. You probably would want to drop it, or maybe keep it, but not kind of, like, as a, you know, source of truth, but maybe only for reference.
Maybe if that customer comes back to you, and you can reference to that. But, so I was just wondering if you have encountered anything like that, and you had to think about the solution.
To this situation, but, it sounds, then no, right? You didn't consider that issue. You didn't count it as an issue.
**Chris Lightfoot-Wild** 26:28 That sounds like, like, a leak… leaking of a, like, a boundary, though.
**Sergey** 26:32 Yeah, in some sense, it's kind of like, yeah, you can say it's even a security issue, because they… there might be a malicious actor that sends you to spam, right, to affect your sampling decisions by sending this transparent header.
So, there might be multiple aspects to that, and you might consider, yes, post-ranging by… from security point of view, or even from usability point of view, because obviously, if you will just continue the trace, you will not have a head of the trace, so depending on what backend you use, some of the backends cannot even handle it, they will not let you see those traces, they don't have the head, right?
Even though you can consider that node that was entry to your org as the head, right? Because that's actually the root spawn for the subtree that you see.
But, I was just wondering if you guys encountered something like that, because we… we… we considered some solutions to that, and we were wondering, maybe eventually even, I mean, even destroying, maybe even contributed upstream, but… I was just wondering if we wanted to gather better and better understand that use case.
We had some guys from Duscan.
**Bob Strecansky** 27:40 It's almost like you'd want to, like.
rename the transparent header to something else, right? Like… ref… ref trace head… ref parent header… ref parent trace, or something like that, you know, something where you know that that trace parent is coming from somewhere else, but you're not using… you're not attempting to use it in the calculation of your, of your distributed trace.
**Sergey** 28:04 Yeah, essentially, that's the… you, in some way, need to define the boundary of your org, right? Because obviously, inside your org, you would like, if you're now renaming, like you said, this to REV, but now you're making new transparent, which you want to continue, you don't want your internal nodes inside your org to do the same, right? You only want to do it once on the boundary.
But then, inside your org, you want to propagate as usual. You don't want to do it on each node, right?
I'm just wondering if you guys ever encountered anything like that, but Yeah.
So it's probably more relevant to orgs that provide some kind of, like, service that is contacted by external customers, like APIs and stuff like that.
**Chris Lightfoot-Wild** 28:49 Yeah, I guess it would be good if there was a mechanism, though, because if there was, like, front-end instrumentation, like, you know, some JavaScript app that was providing that, there's some other mechanism that identifies you can accept traffic from.
random IPs on the internet that are sending you out.
But I guess you'd still…
**Sergey** 29:08 Yeah, that's handled by security, right? You provide them API key and all that stuff.
So, assuming that they already passed the security authentication, that they're allowed to make that request, they already passed that layer, now you are… need just to consider what is the consequences for the telemetry piece.
It's not even about the functionality of the API itself, right?
**Chris Lightfoot-Wild** 29:30 It's good to ask, because it's probably not, like, a PHP-specific question, is it? I wonder if… Yeah, definitely not, that's.
**Sergey** 29:36 That's something that is, telemetry-specific, not… not pitch-specific, yeah, you are correct, yeah.
Yeah, so, just floating it out, I just wondered if you guys had any encounters with something like that, but if you do, let us know.
**Bob Strecansky** 29:52 Yeah, yeah, that's such a fascinating thought process. It's like, you end up with this, like, turtles all the way down of distributed trace of a distributed trace of a distributed trace of a distributed trace, and… It would be cool if you could, like, pass that through, right? Like, if… you… if you had your full distributed trace, and then you could pass it to me, and then I could make a distributed trace on top of that without just calling… like, calling yours in a black box, but that just, like… that gets really messy.
**Sergey** 30:19 I mean, technically, it's probably possible, just, you, you, like you just said, let's treat that parent as kind of like a reference parent, but let's not use it kind of like an authority for, you know, for determining sampling rate and all that stuff.
But maybe if you're ever, like, contacted by the customer, and they want to reference that ID that they sent you, maybe it can be used. So maybe we will preserve it in some way, as some kind.
**Bob Strecansky** 30:41 Oh, yes.
**Sergey** 30:41 Panelink or whatever, but we will not use the authority of determining, like, sample rate and stuff.
**Bob Strecansky** 30:48 I know, like, from industry practice, I've seen the, like, prefix X- used a lot as, like, a… Header modification when you're passing headers, like, between services, so maybe that would be the right thing to do, like.
**Sergey** 31:02 You say, let's do it even external, put some proxy that will do it on the boundary, on the edge automatically, and then we will handle those headers, and we'll record them in some way.
**Bob Strecansky** 31:15 It could be, yeah, that might be a choice. I have to… I have to drop, we'll see on…
**Sergey** 31:19 Okay, thank you guys.
**Chris Lightfoot-Wild** 31:21 Like you, boy.
**Sergey** 31:22 Yep, bye.
