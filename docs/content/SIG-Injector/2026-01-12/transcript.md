SIG: SIG Injector
Date: 2026-01-12
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/Z82JfnsGCBdEpH85DDqdMRQ_AY9hP9E1wcHHQ7kB6Kq4Pp0_ITx0GNcRdcQIEbkf.Pabnsqbao20fvWKd
============================================================

## Zoom Recording Transcript

Bastian Krol 00:01:10 Hey, man. Hi there.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:15 Hey, Westin, how you going?
Bastian Krol 00:01:17 I'm fine, how are you?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:18 Not too bad. Catching up after the holidays?
Bastian Krol 00:01:23 Don't good.
Let's give it one more minute or so to see if Antoine or Michael or anyone else shows up.
That's the last minute cancellation.
Click on.
Yeah, well, okay, I think we can maybe get started.
Hey, Jack, how are you doing?
Jack Berg 00:02:58 Good, how are you?
Bastian Krol 00:03:00 I'm fine.
Okay, so it seems it's just the three of us, so, I, I have one or two quick topics, not sure if you have anything…
On the agenda for today.
Jack Berg 00:03:17 I added a topic.
Bastian Krol 00:03:18 Yeah, just now, at least. Excellent. Yes.
Okay, yeah, maybe I can go first, because that maybe, segues nicely into your question. So,
I released, basically the first non-pre-release, so the first actual
release, this, this weekend, that's version 003, and, I'm planning to integrate this into the zero operator this week, so basically its work's already done, I mean, it's…
more or less very similar code to what we had in Rashivo before anyway, so the change wasn't…
Tibet.
And then we'll roll it out to our… customer base, or…
Of course, that takes a while, because customers update the operator on their own schedule, but slowly, over time, it will get rolled out to our customer base, and that means it will finally… so the official OpenTelemetry injector will finally see some
real-world production usage with, which I think is pretty neat, that's just basically me.
announcing that, and then my question that I wanted to run by you folks is, if we should…
stay with that 00 patch version number scheme? I mean, it's…
basically just optics, it doesn't really matter, but I think we could probably just release a 100 next, or at least a 010, or however we want to do the sentimental versioning there, but…
Yeah. Thoughts.
Jack Berg 00:05:17 Yeah, so my thought on that is,
So, a bunch of areas in OpenTelemetry have resisted going 1.0 for a while.
Because of the stability requirements around that.
And I think it's, like, I think it's overall been a mistake.
There are places where
getting to stability and then not making any breaking changes is pretty important. If you can imagine, like, the APIs, right? So, the OpenTelemetry Java API, or the OpenTelemetry Go API, we're asking all these libraries across the ecosystem to integrate with these APIs, and if we make breaking changes to those, it's very consequential, because now you have this diamond dependency
And, essentially, it, it sort of breaks down the, the trust and, you know, the,
and really jeopardizes the chances that libraries integrate directly with these APIs. And on the other end of the spectrum, you have projects like the collector, projects like the OpenTelemetry Java Agent, and just instrumentation in general.
And, I think, I think, we need to be more nuanced about
Which areas are important to…
get to stable, and then stick with, like, on the same major version, and resist changing the major version, and the APIs are the place to resist that, but projects like the Collector, the Java agent, and now the Injector, and other things of this nature, I think it's good to market as stable.
And… and to,
you know, recognize what things are part of your API. For the injectors case, it's like, there's behavior, and then there's the configuration API. Those are the sort of contracts that people expect not to…
Bastian Krol 00:07:09 Relatively small surface, yeah.
Jack Berg 00:07:11 Right, and, like, you know, we… we should get comfortable with the fact that if we go 1.0, then any changes to those will be, breaking changes… any breaking changes to those would require us to go 2.0. Yeah, and that's fine. That's okay.
Right? In the Java space, we've gotten on this cadence of having a new major version of the OpenTelemetry Java agent once every year. And I'm not saying that the injector should do that, but, like, you know, basically, we're kind of forward-looking, and when we need to make breaking changes to instrumentation because of evolving SEMCOMF or something like that, we sort of, we sort of have next year's major release in mind in bundles
all those together.
And it works out nicely, the one-year cadence for the OpenTelemetry Java, just because the project's really complex and there's a lot of users.
But, you know, obviously for a project like the injector, you could go on whatever cadence you want. But I think having some sort of schedule is helpful. Like, if you need to make braking changes, you know, we don't do it… like, it wouldn't be good for the injector to have, like, a major version every month, for example, or every week to take it to an extreme, but, like…
Bastian Krol 00:08:23 Yeah, sure.
Jack Berg 00:08:24 Quarterly, if needed.
Biannually, if needed, something like that. Just to bundle the changes together and reduce churn.
Bastian Krol 00:08:31 Yeah, so I agree with a lot of what you said, like, especially that my instinct is also just release, 1.00 right now, and, that also gives us a better…
way to communicate breaking changes, I mean, it can also always be called out in the change doc, that's clear, but if you go to 1.x to 2.x, then also the version number communicates that it is a braking change, and we would only do that for a reason, and…
that's… that's how I view that as well,
And we probably have a relatively small number of consumers for now, like, maybe the OpenTelemetry operator in the…
somewhat near future, our operator, and maybe a couple of others, I don't think it will be as widely used as the collector or the…
Java API, or any… any of that,
About the cadence, I'm not super sure if I agree with that, that it should be a fixed cadence. I think it might or as well be as needed. Of course, doing that every week is nonsense, but…
like… if we… for example, I think the next…
big thing that could happen relatively soon-ish, because we are planning to work on that, is Python support.
And I think adding a new language is technically a breaking change.
I think it should be…
communicate it as a breaking change, because then when you roll it out to an existing environment where there already are Python applications that are maybe manually instrumented, or stuff like that, I think that warrants
some notion of, hey, this has an impact on your existing setup. So, for example, that could be
The next major version, maybe.
But anyway.
Jack Berg 00:10:35 That's actually an interesting question, it's like, what constitutes a breaking change for the.
Bastian Krol 00:10:40 Yeah, that's something we need to find out… find out over time, but yeah.
Jack Berg 00:10:45 Right, I think you're right, like, adding a new language,
Adding support for a new language.
For a bunch of reasons, right? So, like, one, it could just be unexpected, and two, the integration with that language,
It could have interactions that we don't understand and break the user's environment, or break the.
Bastian Krol 00:11:07 Absolutely.
Jack Berg 00:11:08 their system. You know, I think we've talked about at one point, like, trying to have some sort of sane defaults, right? Like, if we could, curate the, have some sort of curated or defaults around, like, you know, the new options for,
Bastian Krol 00:11:25 It could execute.
Jack Berg 00:11:26 include-exclude certain processes, right? So that's, like, another thing that, like, we could do, but also a change to those is probably a breaking change. So any changes to
To the default configurations.
Bastian Krol 00:11:44 Yeah, that point.
Jack Berg 00:11:46 And maybe not any, but, like, changes. Some changes.
Bastian Krol 00:11:49 I think, especially if you widen… well, no, that's not true. If you… if you narrow the… so if you exclude some things by default that maybe some users wanted to have instrumented, then kind of… it's kind of also…
Yeah, but I think that needs to be really discussed on a case-by-case basis for each individual change. It's probably hard to give a hard and fast generalized rule on that. Yeah, but for now, so my…
let's circle back to the main question, because also Antoine wasn't there for the start, so I was…
basically proposing that we go to a version that is not 00 something with the next version, and so Jack and me seem to be… have…
agree on just doing 100. I'm not sure what Nicola, thinks about that, or what you think, Antoine.
atoulme 00:12:50 I'm okay with it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:52 I'm cool with that, either, as well. I mean…
The only downside would be if we think adding Python, something would have to happen sooner than maybe…
We go at something 00… One, or whatever.
and then add Python, and then call one.
Bastian Krol 00:13:11 Yeah, that's also fine with me. I don't have a strong opinion either way. I'm not sure how fast we can be with the Python stuff. I know that
other people within my company have started to look at that, so… but I don't… don't know, it's… it's…
my…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:31 Yeah, I don't know how long it might take.
It's fine, it's gonna be 2-0 then.
Bastian Krol 00:13:37 Yeah, so you, you… Go ahead.
Jack Berg 00:13:40 No, I just… I'm wondering if we want to at least sketch out
You know, in other repositories, we have, we have documents about, like, essentially defining what the API is of that repository, and what constitutes a breaking change. And obviously, we're going to learn as we go, but, like, having a starting point to adjust against.
Could be,
a useful prerequisite to having a 1.0.0 release, so at least we're all on the same page about, like, hey.
when we integrate Python, this will or will not be a breaking change.
when we update… I'm writing other examples here, like, when we update the version of instrumentation that's included, like, let's say we update the minor version of the Java agent, or the major version of the Java agent, are either of those cases considered breaking changes that require us to do a major rev… major version rev?
You know, we could argue one way or the other, but, like, you know, if we write it down somewhere, then we can at least be all on the same page.
Bastian Krol 00:14:49 Yeah, that sounds good, I think. I guess there are also ecosystem-wide specifications around that, but I, don't know them from the top of my head. Like…
I guess there's some documentation on versioning.
Jack Berg 00:15:09 There is, but it's always tough to kind of apply it
Okay, yeah. On sort of new cases, right? So, like, if the versioning documentation was written for this idea of, like, distributions of instrumentation, like the Java agent, for example, and, you know, people had that in mind when they were writing what the versioning requirements are. Well, like, how do those…
How does that text apply to something like the injector, which is, like.
not quite a distribution of instrumentation. Like, in some ways it is. It… right now, currently, it downloads and includes, these instrumentation modules as dependencies, but, you know, we could also view that as, like, decoupled.
Where, like, you know, the injector is the injector, and it's sort of like an optional transitive dependency on the OTEL Java agent. And so, you know, we could…
We could probably, if we wanted to,
Fine language to position our versioning as, like, independent from the versioning of instrumentations which we install.
Bastian Krol 00:16:12 Yeah, right.
Yeah, I think I like what you said, like, let's define, what our, basically, stability guarantees are before we go to 100, and then maybe we can also wait for price, and if we have these two things in place.
than the goal.
100.
Jack Berg 00:16:39 That sounds good.
Bastian Krol 00:16:43 Cool. Yeah, I guess that's what my two… list.
atoulme 00:16:49 Maybe a bit of a stretch goal, I know it's…
It's something I worked on, but I never really managed to land, was Ruby support.
I know it's actually not probably something we need to make it a part of 1.0 scope. I think it's nice if we have it. If we don't have it, then we'll catch on. But, it felt like it was in reach. The problem was the testing, and the fact that the Ruby SDK itself, like, the Ruby language SDK was just not…
like, playing along with simple Sinatra-type apps or something like that. So, fortunately.
it's also a thing that I'm recognizing, is that without the language SDK somehow giving us some level of support, you cannot add a new language to the injector that easily.
It can run…
Jack Berg 00:17:36 What kind of support are you talking about? Like, a sort of, like, universality? Like, so, like, you know, if we tried to add Ruby, and it doesn't work for certain classes of Ruby applications, if they just crash, then, like, the injector, we make it unstable by adding Ruby integration, right? Because it makes.
atoulme 00:17:50 That would be helpful. It's not that bad, but it's more like… So, the way Ruby injection would work is that you… it's very similar to Java or Node.js, where you have a Ruby underscore OPTS environment table that you can use to load code as part of a pre-compile type phase.
And, we, we can… we can use that. The problem is that, we don't know…
Like, for Java and Node.js, I have ready-made examples with Stumcat or, like, an Express-type application, and they have pretty solid integrations by now, where those are well-understood.
We're in a, you know, middle of.
Things that everybody's running.
When it comes to Ruby, the main star of the show is Rails.
Which, frankly, is not as nice to run in a unit test type setting, where you would like to create a simple Rails app, and then, you know, start to instrument it. And so I've had discussions with them, where, like, I would like to just run a Ruby app, very simple, just give me… I want to make sure that at least the injector is able to return, like, show the implementation works. And they told me, well…
You need to run the Rails app. Like, I…
I don't know how to run a Rails app. I haven't done that in 10 years. Help me.
Bastian Krol 00:19:03 It's also on the… I mean, Ruby is kind of on the downward path since, like, 5 or 10 years in terms of usage, isn't it?
Just, just in terms of market share.
atoulme 00:19:15 It's nowhere near as important. And also, that… that shows through this, because, in a sense, to me, Ruby is more interesting if it's, like, simple, like, batch scripting, or things like this that are more useful. Okay. If you're going to do Rails monitoring with Ruby in 2026, like…
I don't know. I haven't seen anybody ask me for that before, so this is why I'm tempted to say it would be great to have it, but…
Bastian Krol 00:19:41 Hmm.
atoulme 00:19:42 Besides the SDK offers, if they don't show up and help us, we should probably also move that out of 1.0 at this time.
Bastian Krol 00:19:49 Yeah, let's… let's see about that. So, I mean, what's also interesting is that, I mean, there's this somewhat official
docs about zero code, or zero-touch instrumentation, and Ruby is not listed here. I'm not sure, but you said it can be made zero-touch? Oh, yeah. But PHP.
could still be a valid target. I mean, nobody wants to touch that, probably, with a 10-foot pole, but it still has a very large, installation base, so… just throwing that out there.
atoulme 00:20:28 Okay, that's fair. I actually think this is a valid feedback. It's like, okay, great to have Ruby somewhere, but PHP is much nicer to look into.
Ugh.
Bastian Krol 00:20:38 I'm not saying any… I mean, I guess you would need someone who has really a motivation to do that, and a use case for that, otherwise it's,
I mean, I'm not going to start, working on… on that, just… just really needy, and neither of any of you probably is, but,
It's, it's maybe good to keep in the, in the back of our minds.
atoulme 00:21:03 Yep.
Appreciate that. Makes sense.
Bastian Krol 00:21:12 Jack, do you want to talk about the telemetry operator?
Jack Berg 00:21:17 Yeah, and I really wish that there was somebody… people attending both this SIG and the operator SIG.
And,
I think… I guess to back up for a second, some folks at Grafana, including myself, are interested in accelerating the operator's integration with the injector.
Bastian Krol 00:21:39 And so, yeah.
Jack Berg 00:21:41 I'm just starting to poke around this problem, figure out, like, What needs to be done?
how it needs to be done, what kind of learnings there are from Dash Zero's integration, if there are any. And I guess, like.
this is kind of an open-ended thing. I don't really know where this conversation is going to go, but I just kind of want to feel out this group's thoughts on this. You know, one question that I have in mind is about how when the injector integrates with the operator, the operator's contract has the ability to change for the better.
You know, right now, when you use the operator, you need to explicitly add these annotations to, indicate that pods should be instrumented, and that requirement goes away.
And so that's… that's great, right? Like, that improves the operator. It's also a breaking change to the operator, if we want to switch from a opt-in type of behavior to opt-out.
Bastian Krol 00:22:39 Absolutely.
Jack Berg 00:22:40 Right, so, yep.
Okay, I mean, you guys are saying yes, so that's good. Everybody knows about this, and I assume the operator folks know about this, too, and are kind of looking forward to this?
atoulme 00:22:53 Intimately. Looking forward, no, might be a bit of a strong word.
Bastian Krol 00:23:00 What you, what, what, what one could start out with is,
opt-in to the opt-out mechanism. So, like, have one global switch that says… might be an experimental feature, Slack, that says, instead of
Having the opt-in mechanism where you annotate each workload, please,
just instrument everything, or have an opt-out.
approach where you instrument everything except for ones with an opt-out annotation or something like that. So that could be a slightly more gradual
change it. People can try it out, but it's not forced down everyone's throat, but ultimately, you need to decide on some default behavior, and if the goal is to make it seamless, then probably.
atoulme 00:23:53 defaults.
Bastian Krol 00:23:55 instrument everything is maybe what you want in the end. But that's… that's kind of a product decision.
atoulme 00:24:03 So, I'm gonna give you a lot more context on, the operator of the last year, my involvement with it, but you might, you might, tell me when I get too grain, granular.
I'm going to suggest that first the context is that some of the operator maintainers are members of the Red Hat engineering team, and Red Hat has a very big mission to make sure that people are able to self-upgrade without trouble.
It is really, really important. Actually, that's the main value of OpenShift, is that you have self-upgrades of your clusters, you don't need to touch anything. It's just beautiful.
And we have a lot of customers, we have hundreds of those clusters, and we want to just have a certified Red Hat solution that works with their vendor of choice, that don't actually involve them getting in the weeds every time we make an upgrade. And have had feedback to us, like,
ETCD metrics monitoring broke that one time for a customer. They discovered that a month after, they were extremely pissed.
Is it… was it warranting such level of alarm? Probably not, but then the moment you lose the trust of these type of things, then they get to a point where, like, I want this to work all the time without fail.
So Red Hat is good at this, but they are kind of trailing the community, in a sense, because they're always, like, 10, 20 versions behind. They just can't keep up. It's too much work. They have built their certified version using what is available in open source. So, if you look at the operator, there's two bundles. One is called Communities, the other one is the actual BLEST.
Red Hat one. And so, every so often, they'll push a new version that will use that.
The thing that I took issue with when I started to look at the operator repository is, at first, there was a lot of craft. You can see my whinging and complaining about, like, they didn't have a good interface for configuration, it was inconsistent, it didn't make sense, there was, like, a lot of gotchas, and there were feature gates you could define by a kind of CLI argument, or some via an MVAR.
There's code in there that could leave elsewhere, like the target allocator, to me is not actually related to the operator, it's worth its own project by itself, it's nothing to do with an operator to me.
And so on and so forth, right? So a lot of whinging, a lot of discussions there, and eventually I told them, I find that my customers don't care about how much you like to place in CRDs. If you look at the CRDs for instrumentation, these operator, they're extremely detailed. You can set down to the level of empower for your
you know, Java programmatic instrumentation.
But, what my customers have told me is that we like to set one CRD that installs the CRD's open telemetry.
sets everything up. I don't want to know what's happening. It's happening best practices, so that means we all put our heads together, we come up with the best practices, and we agree we're going to do this. So, for example, this idea of opt-in by default.
would fall into that, because that means that we tell the customers, stay, you know, get out of the driver's seat, we know better than you, we're going to instrument all your Java and Python apps, and you'll like it. And so we built a RFC that we shipped back in July last year.
That was the beginning of that discussion.
Based off that RFC, then we built a pull request that is currently in discussion by one of my people.
So she's… she's working on this since October… November.
You can see it, oh, no, sorry.
here. So, it's in discussion because it's a redesign of where we want to be, right? And…
What it's doing is, in a sense, it's kind of smart. She did not try to build or break everything that the operator does. It's taking the existing CRDs of the operator and saying, hey, we're going to configure them for you.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:53 Mmm.
atoulme 00:27:54 So it's a CRD that define CRDs.
Right? And so, if you were to do an opt-in approach here, this is the right vehicle, because you would just tell people, if you opt-in to this.
it's a configuration thing. Like, you can use the operator however you want, but if you're going to play with us, then use this approach, and we'll take care of everything for you, and we'll apply default basic approaches to everything. So, the injector could come in, we could do a lot of things that are just, like… we just bypass a lot of safety to go straight to where we want to go.
And the final state. And then we use that as an alpha on the operator side to say, hey, you know, we're applying those best practices, what switches are you missing?
What is it that you think we should bring back? What level of control did you want? Did you just want to have…
yeah, like you said, you want to exclude stuff, that's probably a valid one. Did you want to have maybe less control plane metrics compared to what we're going to collect by default? And I can go on, but what I told them is, like, artificially, I'm going to
force you to have no constraints when you start. So I can hear from people adopting it that it's not working in what way? Because we've done the reverse, which is we started to build with legal bricks.
Hoping people would come. That is not working. People have no patience to understand YAML in this year. It's over, right? So, that's…
Bastian Krol 00:29:16 That's super interesting, because what you described there, or what your plans are there, is
quite exactly what we did with the dash zero operator. It started basically with… with zero configuration, or zero configuration
ability, and we just instrument everything how we think, it's probably nice and good. And of course, we got a lot of that feedback that you are looking for, like, then people, of course, come in, okay, yeah, but I really need to configure this and that, and this and that, so…
No matter from which end of the spectrum you come, of course, there's always,
Feedback, that people need things to work differently.
atoulme 00:30:02 Yeah, and then I think it would be a great, good place to help, yeah.
Jack Berg 00:30:05 what I like about this is,
You know, so we've got this sort of…
existing operator, contract, and it has an unknown amount of crust in it. We think it has got some crust, some things that people don't actually need, but we don't know how much. And so you're like, okay, we're gonna introduce something new, something greenfield, call it experimental, call it alpha, whatever it is, and it's gonna be a blank slate.
And, you know, rather than, you know, like, I'm just gonna repeat what you all said, but rather than, trying to collect all this information and decide what people need, we, we use the issue, the GitHub issue mechanism to, to, you know, to collect that feedback directly, start with nothing.
And add it as that feedback comes.
And so what you're saying with, respect to this injector conversation is like, hey, the injector
It… it… it's…
it's complementary to this effort, because part of the existing operator contracts cruft is the requirement to add the pod annotations to opt-in. And so, you know, we kind of… we do these two efforts at once. We simplify the configuration interface, have it all in one place.
And we introduce the injector and all of its, you know, newness and, like, potential instability, and we kind of bundle all that churn together.
atoulme 00:31:34 Yep, you got it.
It's tough.
Bastian Krol 00:31:36 Sounds pretty good.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:37 I had a…
Bastian Krol 00:31:37 Closed.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:38 sort of comment, if you don't want.
First, I have a question. I believe that the operator allows you to set a namespace
annotation to instrument everything on ASpace. Is that true? I think they added that.
atoulme 00:31:53 Councilmember. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:55 But I would like to say that one thing we need to be a little bit concerned about is, if we go with this approach, instrument everything, we should not add go.
Because a lot of the…
Kubernetes services that run Kubernetes are written in Go, including the auto collector and everything else. If you say instrument everything, it will go and instrument the system namespace and everything else that comes with it. So, definitely causes a problem.
atoulme 00:32:23 Yeah, we don't support Go. I think, mostly, we're going to look for interpreted languages like Java, Node.js, Python, which are the meat, and where our customers play more.NET, of course, as well, is a big one. And if you get those four, then you get 80%, and then we…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:40 Even more, yeah.
atoulme 00:32:41 I want… I want people to clamor as, like, my PHP app is not showing up in my applications, I want to hear someone say that.
Bastian Krol 00:32:49 Yeah.
atoulme 00:32:50 I wanna hear this thing.
Bastian Krol 00:32:52 I mean, about Go, the discussion comes up every once in a while, and we also, I think, discussed whether we want to somehow integrate OBI with maybe the injector or not, but I think that's really a discussion for much, much later. And if we ever go there, then of course, we need to
have good defaults for excluding the system namespace, the collector itself, etc, etc, but I think that's something we really don't need to worry about in the next year or so.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:21 Okay, alright, good. Yeah, because OV right now, if you look at it, there's the default exclude policy, and it contains all these expressions to kind of exclude everything that you possibly find in the world in Kubernetes, including AWS and…
Bastian Krol 00:33:34 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:34 And all sorts of stuff, because you play it in, it's go, and it just goes mental and instruments, everything people add to Kubernetes.
atoulme 00:33:43 Yep.
I expect our friends from OpenShift are going to actually be a good, kind of.
bulwark for these type of things, because they will give us the feedback we need.
And we're clearly optimizing for OpenShift Red Hat, right? We're really trying to get them to a top-notch premium solution that is going to give them, frankly.
What I don't want is to build a vendor solution for OpenShift.
I want Red Hat to support this, and I want this to be a vendor-neutral approach that works with every vendor out there that is OpenTemmetry compliant, and this way we reduce the friction we have with our customers, with Red Hat, with everybody, because we don't have time, and we don't have
frankly, the means to have our hands into a Red Hat, certified operator. If you know how much work that is, it's not… it's not something I'm interested in. I think my team is not.
it's not going to do as well, and Red Hat's kind of tied up otherwise, because they have to support us too, right? So the moment they certify us, they're tying their fate to us, and I don't like it. I think, again, like, going back to open source, right? This is how we're going to grow the pie, by having a more standard solutions that work better.
Jack Berg 00:34:55 One, so I wear multiple hats in OpenTelemetry, and I like what we're talking about here with starting with a blank sheet of paper and adding configuration options as requirements come in.
That is intention, and what I'm seeing in this, like, this PR here is intention with this other hat that I wear, which is… I lead the declarative configuration SIG, because what I see here is, like, an attempt to create, like, a minimalist
SDK configuration, DSL, structure, whatever you want to call it, which is, you know, duplicating the efforts of declarative config. And declarative config is, like, you know, it's a more verbose syntax,
And, you know, we've discussed whether that's necessary or not, and I think, you know, the TLDR is that, yes, it probably is necessary for… to have that verbosity, but, like, because the verbosity lends itself to, like, completeness, and, and, you know,
helps you avoid these sort of unintuitive outcomes. But, like, yeah, how do we reconcile these things? Which is, like, you know, users want simplicity.
And the operator wants simplicity, and wants to, like, add features as users request them.
And, you know, on the other end, OpenTelemetry does not want more configuration APIs. Like, in some ways, the existing operator's configuration API, which is, like.
I don't know what we would even call it. It's sort of like an unsanctioned configuration API that it, like.
atoulme 00:36:35 Yes, that's what I found out when I started to play with it, is that people were adding booleans and whatnot flags into this, and there's a V1 alpha 1, V1 beta 1, this and that. It's just not super nice for people when they want to, kind of, work in this system.
Operators are not friendly in the first place, but defending a piece of YAML that's going to leave in your Kubernetes cluster and do magic things? That's even less fun. Like, it really is not.
bleh.
Yeah.
Michele Mancioppi 00:37:04 And it's also a piece of YAML with very many jacked pieces, and you need actually to understand how injection works, to figure out all the possible failure modes of what it's doing. It's a bit of a dire experience.
atoulme 00:37:19 Yeah.
Jack Berg 00:37:20 Yeah, I just sent the link over, and, you know, this is… this is, you know, the… from the operator's docs. We're all familiar with this, but, you know, this is the operator's docs about how you configure instrumentations, and it's like this…
this weird structure that somewhat mirrors the environment variable configuration interface, but deviates it in important ways, and it just seems like it was sort of Frankensteined together over time, without, like, clear principles about, like, you know, all the things that you can do with it, and why, and how, you know, versioning works, and things like that.
atoulme 00:37:55 They tried their best. They tried earlier than you started. That's the problem.
Jack Berg 00:37:59 Exactly. They tried… they tried earlier, and, you know, they were trying to create something that was useful, right? And, like, what I've been working on is something that is, like, like,
indexed on long-term, evolvability, right?
atoulme 00:38:16 If you want to hear people, lament, we had had multiple sessions where we just… we were holding a beer at this point, like, this is terrible, how do we handle this? What are we doing? Yeah, yeah.
Jack Berg 00:38:29 Well, I wonder if this Greenfield opportunity is an opportunity to have a clean slate, and, like, we want a minimalist configuration API, but, like, maybe we could adjust what our definition of minimalist is. Like, you know, the configuration API covers a number of things. It covers things like which languages are instrumented.
which processes are instrumented, what the SDK's configuration is.
when an instrumentation is installed. And, like, maybe we could have a, like, simple be the goal, and minimalist be the goal for this, like, this overall configuration interface, and… but still find a way to delegate to declarative config to not duplicate efforts.
atoulme 00:39:11 I used a different word when we did the RFC. I said opinionated. I said, this is not minimalistic, or good, or… no, this is us expressing an opinion. This is what it's going to be, and you're gonna have to like it. And if you don't like it, we're gonna have to have you engaged to talk back to us. I think these are, also going to the product versus project discussion that we've had at the OpenTeometry level. Yeah. If you want to build a product.
You're gonna have to make trade-offs.
And you're gonna have to come down hard on some requirements and say, this is how it's going to be, and you're going to like it. Back to Michael's point about having an open telemetry APT package. Same thing. We're gonna have to leave stuff out, and we're gonna have to make stuff in and make it default, and people are going to have.
Michele Mancioppi 00:39:53 I have an opinion about that.
atoulme 00:39:56 Yeah, Mika, yeah, go ahead.
Michele Mancioppi 00:39:58 The, so something that I would really like to work into the APD packages is for them to treat the declarative configuration format as, the default.
And…
atoulme 00:40:11 The, I believe that in general, we can have.
Michele Mancioppi 00:40:15 Presets, potentially based on the language.
I have not spent enough time looking into how consistently the configuration language has been implemented.
Across the different SDKs? Just a second, I need a second.
atoulme 00:40:31 Yep, nice.
Michele Mancioppi 00:40:41 kids broke a glass and are screaming. Excellent. So…
atoulme 00:40:47 Nope.
Jack Berg 00:40:56 Hmm.
Michele Mancioppi 00:40:59 Alright, so,
The, I would love for the configuration format to be… to be implemented consistently by this case, and then we treat it as a first-class citizen.
atoulme 00:41:10 I am not sure what you should do in the middle term.
Michele Mancioppi 00:41:13 when important SDKs like Pythons, to the best of my knowledge, they don't have any support for it yet.
Bastian Krol 00:41:19 I think it's only Java right now, huh?
Jack Berg 00:41:22 There's, like, 6 languages that are in some form of progress. Java's leading the way, Go's pretty good. JavaScript is getting pretty good.NET has some people working on it. PHP has a person working on it.
Bastian Krol 00:41:39 Okay, never mind then.
Jack Berg 00:41:40 But, like, but, you know, I think the point is still a good one, right? So, like, it's still not ready to… it can't solve all of your problems yet. It will, like, once it gains enough momentum, it will be the way to go, but we have to meet people where they are right now.
And so, I wonder if in this opinionated configuration interface that the operator wants to have, like.
There's two paths.
There's declarative configuration for the SDK, and there's environment variable configuration for the SDK. And you can choose one or the other, but not both.
And if you… if the operator is, you know, doesn't try to create its own configuration interface for SDKs, if it's just like, hey, we're gonna give you environment variables or declarative config, you choose based on
The maturity of those tools based on the languages you're using, then, you know, it can still remain, like, minimalist or small in surface area, and still accomplish a lot.
And not get itself in a… Defined that it has today.
atoulme 00:42:45 Okay.
Jack Berg 00:42:48 Like, why did the operator.
Michele Mancioppi 00:42:50 The other environment variable.
You're valid, right?
Jack Berg 00:42:56 Could you repeat that? I think I… I interrupted you.
Michele Mancioppi 00:42:59 I believe that…
If you pass today the otel underscore config underscore file environment variable, which is the opt-in to declarative configuration file, the environment variable-based configuration is ignored.
Right?
Jack Berg 00:43:15 That's… that's the way it's written, yeah. That's the way it's spec'd out.
Michele Mancioppi 00:43:20 Writing the spots.
Jack Berg 00:43:22 Yeah, yeah, and it sort of matters, like, because your environment… your declarative config file can reference environment variables, and so, you know, those environment variables will still have meaning if they're referenced in using the substitution syntax. But, you know, depending on what the contents of your file are, you know.
The environment variables may or may not do anything.
Michele Mancioppi 00:43:52 Yes, so the,
what I had in mind for the integration of the OpenTelemetry injector with the configuration file is the fact that users will be able to opt-in
But on a language-by-language basis, about whether they want to use a configuration file.
If that is the case, there is a default location where we ship default configuration files for all the languages.
And then allow… the,
Allow the override of those files, both by the user, pointing with the environment variable into a different configuration file.
Or not.
effectively, that is the way I would do it at first. I was thinking about other possibilities, and this strikes me as the best trade-off between
flexibility, supporting the configuration file, and not reinventing the wheel with yet another configuration. Because it already pains me that we have our own config… our own file format with information about .NET and other stuff that.
atoulme 00:45:07 I feel we shouldn't have.
Michele Mancioppi 00:45:09 In the injector.
atoulme 00:45:11 No.
the same sphere.
Jack Berg 00:45:17 Yep.
atoulme 00:45:21 So, Jack, it's kind of up to…
Do you want the declarative config sig to kind of, start to kind of,
kind of amp up its efforts to become kind of the product requirements, in a sense, like, this is how you're going to interface with users, and this is… they're going to like it, because it's going to be that simple.
Is that… I think that's the… the object… the objective of that SIG, right?
Jack Berg 00:45:45 So, the objective of the SIG, you know, is to introduce
you know, all the tools you need to have a structured configuration interface that is consistent across all the languages in OpenTelemetry. And, you know, we're actually trying to shut down the SIG after we get to stable.
atoulme 00:46:05 Yeah, sure, why not?
Jack Berg 00:46:06 Like, because… not to say that configuration work ends, but, like, we want to, we want to, like, end projects in OpenTelemetry, and if there's new work to do after we achieve this, like, this long goal of getting to stable, then we want to recharter.
Right? Like, start a new issue in the community SIG, talk about what the new goals are, get the people together. Awesome. Right, so, but, like, you know, the… it's…
you know, the configuration interface, the data model, and, you know, the tools around it, I think they're… they play a really important role in this, like, you know, open telemetry as a product story, because you can't really have a good story around that. Like, you can't have a good injector, you can't have a good operator story.
without the declarative config piece. It's the sort of key that unlocks that, or it's one of the keys that unlock that. There's, like, 3 or 4 things that need to come together to have a really great open telemetry product.
we're… and declarative config is just one.
atoulme 00:47:09 Okay.
I think we're all pacing… we're all trying to drive to product requirements and to drive to a product experience for Penteometry, but we're just… it looks like the GC has the intent and sets the high-level goals, but there is no…
no one actually driving this. We have a packaging SIG discussion, but then we don't have people driving this. We have zero SIG, but people are marred into having to maintain the existing codebase. We have the injector SIG, but we're trying to kind of
you know, leapfrog from unstable to something that people would want to use, and that's why we're talking about 1.0.
And I think the GC has set a line in the sand around KubeCon NA, where they said, okay, we're gonna have to move towards a product experience discussion and have more of a stability and all the stuff that went into the blog post, but there's no teeth to that. So, who's responsible?
And I'm sure you're gonna point yourself. Sorry about that. Who's responsible for driving this? And is there maybe a SIG that is missing, or is there a way to organize ourselves that hurts less?
Jack Berg 00:48:16 This is a cross-functional project, and cross-functional projects are hard, you know, when you work within an organization that has clear roles and responsibilities and hierarchies, and in open source, we don't have those, we don't have
you know, people obligated to do anything. And so, a cross-functional project in open source is going to be especially difficult.
atoulme 00:48:37 Yeah, I've seen Doug. I've seen,
I see the Eclipse Foundation do a release train, and kind of woo people by saying, hey, we're going to, we're going to have a release train, would you like to be in it? Because this way you get more people to try your stuff.
and kind of do this from an advantage point of view. But, you know, of course, Eclipse is a very different community with a lot of IBMers who are more like, okay, I get this, I like this because it's more familiar, right?
We don't have too many people who are, complete open-source, you know, anarchists, but we certainly have a more varied population. But let's just point out, it's like, we don't have someone who's, like, we don't have a group of people right now responsible for the product discussion, and we're having those product discussions in every other SIGS.
And then, yeah, to your point, it's cross-collab, but… Yep.
Michele Mancioppi 00:49:28 If it's, if it helps.
Bustin Kroll and I are going to go to, Fostom, the Auto Unplugged.
trying, actually, to… to get interest around the cross-collaboration with the configuration file, the SDKs, and the injector. I do not believe that it is sustainable for the
in Jeter SIG to do packaging for SDKs.
Because nobody else does. I mean, the only one that would work out of the box, literally, is the Java agent one, because it's a JAR file. All the rest needs packaging.
atoulme 00:50:08 Yeah, that's great. That's… that's… that's really awesome.
Jack Berg 00:50:13 I'll be at the Hotel Unplugged as well.
Michele Mancioppi 00:50:16 Then maybe we can show to many, many voices that this needs doing, and it needs the SDKs to…
atoulme 00:50:23 To help, and at least to not break stuff.
Bastian Krol 00:50:26 Cuckoo.
By the way, I mean that, OTL Unplugged will be an unconference format. I think we might want to prepare a little bit, like an elevator pitch or something like that, that we can have ready if we…
Get a chance to… to start a discussion or something like that, but…
atoulme 00:50:47 Yeah, that's a great idea. There was, actually, last week,
You know, we talked, we talked with, there was, the day after Operator SIG, sorry, Injector SIG, there's a maintainer sync at 8 AM PAT that, happened, and, there was a call to action on the maintainers and the language maintainers, so let me try and find the notes.
That might be a great, like, frankly, copy-paste that.
Bastian Krol 00:51:18 Awesome.
atoulme 00:51:19 Yeah, where can I find this stuff, though?
Zig, zigzag.
I'll find it and put it in the notes.
Bastian Krol 00:51:29 Yep.
on Slack.
atoulme 00:51:32 That works, yeah.
Oh, I funded.
A little bit here.
It was by Meghdad.
So, here, I'm implicit in this chat right this moment.
Can I?
Can I send that?
Thank you. Okay, it's not very readable. Here is the doc, he went with it.
And it was to read all that, defining the entire project roadmap for language SIGs. We had some off-stars, we'd like to consider practice. SIGs are not in the same place, they might be working on earlier stages. How do we find the balance between shared goals and working on language-specific issues? Can a liaison program help?
Every SIG should have a charter that is renewed, maybe on a yearly basis or something like that. That includes a roadmap that is reviewed and approved by GCNTC. There will be the opportunity to discuss and find common goals. There will be a sync point with very few of them between SIGS and leadership at this time. It would be great to hear from maintainers. Please come next week, or DMTED. So there is, this outstanding meeting is every Tuesday at 8.
I would continue that pitch.
Right? Let's not split the signal. I think this is a good deliver to pitch for what the injector is also facing, right? This problem of pagmentation.
Michele Mancioppi 00:52:53 I also feel that if we are…
If we take the time to do the packaging in a way that are modular, I'd support for a couple of
A couple of languages and put out a good beta.
people will see the value of that. It's gonna be a much easier sell.
Then go into the language 6 and say, hey, if you did the packages that don't suck, then maybe we can work together.
And this is why we agreed with the, project.
file that we wrote with Ed to actually have the first version, and I'm thinking that we need to sell it internally in the project better now.
Jack Berg 00:53:31 I think the operator could be… this sort of operator refresh could be a good, forcing function to align all these pieces.
atoulme 00:53:43 In these different groups.
Jack Berg 00:53:45 Right? So, if you think about it, the, the operator, and let's think about, like, Jinja 2, this proposal over here for, an opinionated operator configuration, which has all these benefits over the existing, kind of, crafty one.
You know, but it depends on a number of things. It depends on the injector. It depends on instrumentation being good. It depends on declarative config being integrated in these languages. It depends on the operator maintainers, and a couple of other things. And so,
You know, I don't think we can wait for all of those pieces to be in place.
To deliver something, but, like, if we can deliver this skeleton of…
of, you know, this kind of vision of what the operator could get to, then we can kind of identify what the missing pieces are, and then have a really good incentive to go and build those pieces. So, you know, if we say, like, look, this new operator story is great, but, like, it's not so great for .NET, because they don't have declarative config support.
Go build that, and here's why.
atoulme 00:54:50 The new operator experience is great, but it's not so great because the Node ecosystem has shitty instrumentation.
Jack Berg 00:54:57 okay, go build that thing. And, like, you can kind of chip away at the missing parts to having a great product experience, and if you… if you apply that enough times, for enough time, then eventually, you know, you'll have something that is complete and, you know, and very useful.
So, I guess I'm trying to find a way to kind of coordinate across these groups.
Without, getting everybody all there in one place, and to agree.
atoulme 00:55:26 Ha!
Okay.
Michele Mancioppi 00:55:29 I mean, the injector is something that… We built… So deep.
it came together between Antoine and Darshita, but ultimately, it was born to live in the Darshita operator for Kubernetes, and we know it will work a treat in the OpenTelemary one with relatively little changes, I feel.
the, antoine, do you feel… do you think there…
Far enough to try and push it upstream.
To the… not upstream, but downstream to the operator?
atoulme 00:56:07 Yeah, I think so. I think it's time. I think especially because you've made the biggest changes there about the way that you're flipping the getEnv now, it's ready. You have a PR that's been draft to…
try that out before, Michele. So, I'm kind of, deferring to you on that, but if you want, we can…
Michele Mancioppi 00:56:27 PR is… I mean, I have not checked how much the operator machinery changed inside, but the factory… the contract of the injector has not changed on one Iota.
atoulme 00:56:39 And I don't know. I tried, by the way, because, that's a discussion not for me, for Jacob Arunov.
he's been trying to kind of change the way the operator works, because it's actually really bad at scaling up past 2,000 pods, in terms of, impact. I don't know if you…
If you're familiar with that. But the operator, currently is ham-handing, stuff, because it's currently listing and reading, CRDs defined in your cluster constantly. So there is actually a need for a pretty deep
re-cut into the operator code to change the way it behaves.
the webhook is not done proper. Like, it should be caching the CRD definitions, and it's reading them from the API server every time a pod starts. So, you can imagine what that does at scale, right?
So we… Jacob knows about that, he opened a… he opened some branches to kind of work on that back in September, then he's switching jobs, and things kind of get,
piled up on that. I haven't been following the operator very closely in the last 6 months, but it hasn't seem to be changing that much.
There's a lot of work just to support and maintain this code, anyway, because between Kubernetes versions, you just have this stuff.
Another thing for you, Michaela, is that you remember when I was whinging about Docker images as volumes? Now, it's enabled by default as of Kubernetes 134.
Michele Mancioppi 00:58:06 Which is… it's still in beta, right?
atoulme 00:58:10 Better, but it's enabled.
Michele Mancioppi 00:58:12 That is something we need to… we need to play with.
atoulme 00:58:15 Yeah.
Yeah, because that changes everything about the way we mount stuff.
Michele Mancioppi 00:58:20 Not really. It's, the images as we use them today, they are absolutely reusable, you just…
You just do not care about the entry point script.
atoulme 00:58:32 I mean, it changes the base image, because right now they're using BusyBox, which has licensing issues, as part of the base image for their current SDKs, and we would be able to do away with that, which I want.
Michele Mancioppi 00:58:42 Yeah, but it's, I mean, for the foreseeable future, Antoine, it's gonna take a few years until.
atoulme 00:58:48 Oh, God. You are guaranteed.
Michele Mancioppi 00:58:49 that all the Kubernetes clusters are…
atoulme 00:58:51 Aren't that far.
Michele Mancioppi 00:58:52 And before, like, the volume, image volume, I think it was in alpha since 128 or something like that, but it's obtained in earlier versions.
So… but I don't think PCBox is going anywhere.
atoulme 00:59:07 Ugh… Okay, well, I wanted to express some hope, but you got me back to her. Thank you.
Michele Mancioppi 00:59:14 No, we should try it, because there are great improvements to be had, much less anytime you don't need… in that case, the… I mean, of course, the files are… they're going to be served by memory, but it's not a copy of the memory twice. There are very nice things going on there.
atoulme 00:59:31 Yeah, finally, right? So…
I think there's some level of refunding of this code that we would want to kind of play with. And frankly, we need to prepare for that. Even if we don't have it by default, I would like it to have some art, like, test it out, maybe a feature gate or something, so we can try this when the time comes, we can start.
Michele Mancioppi 00:59:51 I will, we'll actually start experimenting with that in the, DC operator.
So that you can… now we can test it, across… well, first internally, and then across every customer, see… see how it works. And we will need, of course, to keep it backwards compatible.
atoulme 01:00:11 My bow to you, if you… if you get to try this, that's great for you. No problem.
Yeah, so, let's… lots of work, but the current… the… no, the machinery has not changed, we need to change it, and,
We need to have the operator care a lot less about what's happening in the instrumentation phase currently. The operator is forcibly taking action by manipulating environment variables, or importing files in the right place because it's Java or Node.js, something like that, and that needs to stop. We need to have it, so it's just delegated to the injector.
Michele Mancioppi 01:00:46 Speaking of languages, so, we will be looking, soon in their zero to add support for Python.
Python is, I mean, you know, it's the favorite SDK I like to… To… to step on.
Today, I was looking… so did there…
Crazy issues in terms of, internal startup time and the dependencies with,
protobuf and the rest of the nonsense, but we think we'll take care of that. We don't know yet how long it's gonna take us. But I was wondering if somebody else actually is interested in adding support for Ruby.
atoulme 01:01:29 We talked about that before you got here.
Michele Mancioppi 01:01:32 Alright. So…
atoulme 01:01:34 Not my customers, but the Ruby SDK, at least maintainers, were interested, right? And that was…
Michele Mancioppi 01:01:40 That'll be really cool.
atoulme 01:01:41 Yeah, there's a PR open up against the operator, where it didn't get as far as I wanted. I mentioned to the team here that the problem I had when I was trying with Ruby is that I could not get it to a test that I could reproduce and try.
Because the only thing that the Ruby SDK is really going to support is Rails, and because you can imagine, testing a Rails app is just like, okay, so I need a… I need a proper Docker image where I run a Rails app, where I…
Michele Mancioppi 01:02:09 I'm pretty sure that if you ask Claude nicely enough, it gets a hello world.
atoulme 01:02:14 There you go. No, I tried Hello World, but yeah, maybe, yeah, you're right. So, I didn't get that far, it's not my forte, I haven't done Ruby in 10 years, I used to be pretty good at it, but it's gone. So…
if one… someone else wants to try it, there's some previous work. And it's not, like, very far from Node.js or Java support, because they use Ruby underscore PTS as a way to inject, and the maintainers of the Ruby SDK tried to implement it into the operator, so he's done the legwork of
Documenting how that auto-transformation works there.
So you can… you can use that prior art and probably get a heads up, like, get, like, way pretty far into it. I had a PR op-ed for the injectors that would get you there too, but the problem is, I don't have a test that works.
Michele Mancioppi 01:03:02 Hmm.
Okay.
atoulme 01:03:04 Oh, yeah, if you want to try, like, feel free to clone my PR and do something else.
Michele Mancioppi 01:03:10 Speaking of which, so, Ruby then, it's maybe not in the short term.
I'm pretty certain that the, OTLP, HTTP exporter.
So did Python, among the various things. It's missing an HTTP JSON exporter.
Yeah. And, the, HTTP protobuf exporter.
has the most toxic dependency you can imagine, that is the Google RPC, and…
Dear Antoine, you said you would speak with your Pythonistas?
atoulme 01:03:51 Yeah, and then what happened is that, so, our Pythonistas, if you look around for where they are spending their time, they're spending their time on AI SDKs, because that's where the money is these days, I'm sorry, and so they're about…
Michele Mancioppi 01:04:02 We cannot inject… we cannot inject the SDK with dependencies to the requests package of a version from…
atoulme 01:04:10 Before the wheel was invented round, and Google Protobf.
I'll ask again, but we had a guy who was probably the best person for this, but he's on leave, so I did not manage to get the buy-in. Sorry. So…
Yeah, don't… don't put your hopes on me. I need this to be an SDK issue.
Michele Mancioppi 01:04:32 Yeah, who am I going to put it on? The Python SDK maintainers that have had 3 PRs open with something like that over the years and merged exactly zero of them?
atoulme 01:04:41 I think so, I think we need to show up at the Python seed and say, hey, your stuff is unusable.
Have you… have you went…
Michele Mancioppi 01:04:48 Going to go great.
atoulme 01:04:50 Did you go to a Python Sig meeting? Oh my god. You know, I do this all the time, I mean, I'm nice here, but I'm… I'm French on some other meetings, you know?
Michele Mancioppi 01:04:59 Go in French all over them, Antoine.
atoulme 01:05:02 Okay, I'll try. If I… I'm closer to that, I'll try now, but I don't want to put any promises here. I've relayed your message.
it didn't go well. So, I need to… yes, it needs to be a bit more, frankly, loud.
Michele Mancioppi 01:05:18 Because I was tempted to actually go and corner somebody physically at the end conference.
atoulme 01:05:24 Do it! Why not do that?
Michele Mancioppi 01:05:26 I don't support that.
atoulme 01:05:28 You don't have to bother them, you just need, you know, hey, what's up?
Michele Mancioppi 01:05:30 Sebastian, don't worry, you get to check if anybody's coming, like, you won't have to be personally involved.
Bastian Krol 01:05:36 I want not to be, put in jail in Brussels.
Michele Mancioppi 01:05:42 I gotta… I gotta run, folks, I… Alright, bye folks.
